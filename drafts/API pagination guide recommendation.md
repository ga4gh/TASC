# API pagination guide recommendation v3

**Source**: TASC

**Recommendation**: GA4GH-NN

**Title**: API pagination guide

**Related GitHub issues**: [TASC#29](https://github.com/ga4gh/TASC/issues/29)

**Author**: Mamana Mbiyavanga, Andy Yates

**Date:** 2023-11-27

## **Abstract**

The recommendation is a summary of the discussion at the London GA4GH Connect to describe the pagination methods employed by the Tool Registry Service, Beacon 2 and Data Connection GA4GH standards [AGENDA] [PRESENTATION]. It highlights approaches to implementing pagination called offset-based and token-based, and documents how pagination logic may be encoded in a server response. Offset-based and token-based pagination are the two approved GA4GH preferred strategies, with guidance around how to implement these strategies and their applicable use-cases. If an implementation requires authorization, it must be applied to every paginated request. This recommendation does not require existing GA4GH standards to reimplement their pagination strategy.

## **Status of recommendation**

Draft

**Table of contents**
- [API pagination guide recommendation v3](#api-pagination-guide-recommendation-v3)
  - [**Abstract**](#abstract)
  - [**Status of recommendation**](#status-of-recommendation)
  - [Recommendation](#recommendation)
  - [Purpose of pagination](#purpose-of-pagination)
  - [Pagination method recommendations](#pagination-method-recommendations)
    - [Offset-based pagination](#offset-based-pagination)
      - [Parameters](#parameters)
      - [Body response](#body-response)
      - [HTTP Response codes](#http-response-codes)
      - [Example implementation](#example-implementation)
    - [Token-based pagination](#token-based-pagination)
      - [Parameters](#parameters-1)
      - [Body response](#body-response-1)
      - [HTTP Response codes](#http-response-codes-1)
      - [Example implementation](#example-implementation-1)
    - [Security](#security)
    - [Consistency of results](#consistency-of-results)
  - [Use cases](#use-cases)
    - [Use case: random seeking within a result set](#use-case-random-seeking-within-a-result-set)
      - [Use offset-based pagination](#use-offset-based-pagination)
    - [Use case: parallel block retrieval](#use-case-parallel-block-retrieval)
      - [Use offset-based pagination](#use-offset-based-pagination-1)
    - [Use case: streaming large result sets](#use-case-streaming-large-result-sets)
      - [Use offset-based pagination](#use-offset-based-pagination-2)
  - [Pagination logic](#pagination-logic)
    - [Client side driven logic](#client-side-driven-logic)
    - [Server side driven logic](#server-side-driven-logic)
      - [Parameters](#parameters-2)
  - [Considerations](#considerations)
    - [Existing GA4GH standards implementing pagination](#existing-ga4gh-standards-implementing-pagination)
  - [References](#references)


## Recommendation

Existing GA4GH standards use a variety of pagination approaches which have been documented briefly below. GA4GH supports two types of pagination; token and offset based pagination. A new GA4GH standard SHOULD NOT use another pagination method without prior discussion with TASC. Offset-based SHOULD be used when random seeking into a result set and when client querying flexibility must be retained. Token-based pagination SHOULD be used when streaming large multi-paged responses. Implementations MAY encode pagination logic into their responses. Existing standards are not subject to this recommendation.

## Purpose of pagination

Pagination allows clients to retrieve data in smaller, manageable chunks instead of receiving an entire result set in a single response. It intends to improve performance, reduce the size of result payloads, and to enhance user experience. In addition, pagination provides a structured approach to navigating data, making it easier to process, display, and analyse information. Regardless of the pagination technique chosen, a set of consistent parameters to control pagination in an API should be defined. The structure of the paginated response should follow a consistent format to aid clients in consuming the data as is detailed in this document.

## Pagination method recommendations

### Offset-based pagination

Offset-based pagination enables page random seeking by combining the limit parameter and page offset together, e.g. to retrieve records 11-20, a client may construct a query specifying offset 2 and a limit of 10 records. Servers SHOULD provide the total number of records to facilitate easier client-side pagination. Offset-based pagination is available in many backend stores and public APIs such as GitHub [GITHUB]. Additional concerns about implementing good offset-based pagination are mentioned in other style guides, such as providing hints as to when the server response has been exhausted and no other pages exist [MICROSOFT].

#### Parameters

Offset-based pagination requires two parameters to control the paging of data. New GA4GH standards MUST limit the use of parameter names to the ones specified here.

- **limit** - The maximum number of records to return in a payload
- **offset** The page offset to retrieve. Numbering MUST start at 0. Not specifying an offset in a request assumes the first page i.e. 0.

The parameters SHOULD be encoded as a URL parameter or POST body payload (depending on the implementation’s requirements).

#### Body response

After a successful response, the server MUST respond with the limit and offset used in the request. A server MAY respond with the total count of results. The names used should match those specified here:

- **limit - The specified number of records to return in a payload**
- **offset** - The page offset requested
- **total** - The total number of results available in the result set

#### HTTP Response codes

A valid pagination request SHOULD respond with a 200 (Success) HTTP code.

If a client requests the final page with a limit in-excess of the final set of results an implementation SHOULD respond with a 200 (Success) HTTP code.

If a client requests an invalid page (requesting a page which is beyond the results available), the server SHOULD respond with a 400 (Bad Request) HTTP code.

#### Example implementation

Send a query to a server with a limit of 10 results: [https://example.org/api/endpoint?query=abc&limit=10](https://example.org/api/endpoint?query=abc&limit=10)

The server will respond with a 200 code:

```json
{
  "results" : [
    ...
  ],
  "pagination" : {
    "offset" : 0,
    "limit" : 10,
    "total" : 16
  }
}
```

A follow up request: [https://example.org/api/endpoint?query=abc&limit=10&offset=1](https://example.org/api/endpoint?query=abc&limit=10&offset=1)

Gives another result set with a 200 code:

```json
{
  "results" : [
    ...
  ],
  "pagination" : {
    "offset" : 1,
    "limit" : 10,
    "total" : 16
  }
}
```

Sending in another request such as [https://example.org/api/endpoint?query=abc&limit=10&offset=2](https://example.org/api/endpoint?query=abc&limit=10&offset=2) will result in a server 400 response as we have exceeded the maximum page size.

### Token-based pagination

In token-based pagination, a client passes a unique token which, when given to a server, specifies a page of data. Tokens SHOULD be opaque and are not intended to be interpreted by a client. When responding to a request for paginated data, the server response MUST include a token for the next page of data. The server MAY also provide tokens for the current and previous page of data.

#### Parameters

- **token** - The token representing the next chunk of a result set. MAY be omitted from a request if this is the first request.
- **limit** - The maximum number of records to return per request. An implementation MAY choose not to implement or honour this parameter

#### Body response

After a successful response, the server MUST respond with the token to use in the next request. A server MAY respond with the total count of results if known, the limit used if honoured. The names used should match those specified here:

- **limit - The specified number of records to return in a payload**
- **next_token** - The token to use to request the next chunk of the result set. SHOULD be null if there is no subsequent chunk
- **total** - The total number of results available in the result set

#### HTTP Response codes

A valid pagination request SHOULD respond with a 200 (Success) HTTP code.

If a client provides an invalid token it SHOULD respond with a 404 (Not Found) HTTP code.

If a client passes a previously used token, the server SHOULD respond with a 400 (Bad Request) HTTP code if the request cannot be honoured, a 200 (success) if the data can be served and a 404 (Not found) if the token has expired.

#### Example implementation

Send a query to a server: [https://example.org/api/endpoint?query=abc](https://example.org/api/endpoint?query=abc)

The server will respond with a 200 code:

```json
{
  "results" : [
    ...
  ],
  "pagination" : {
    "next_token" : "abcdefg",
    "total" : 16
  }
}
```

A follow up request: [https://example.org/api/endpoint?token=abcdefg](https://example.org/api/endpoint?token=abcdefg)

Gives another result set with a 200 code:

```json
{
  "results" : [
    ...
  ],
  "pagination" : {
    "next_token" : null,
    "total" : 16
  }
}
```

### Security

In the case of APIs which require a client to provide authorization to access a resource, that authorization should be required not only on the initial request, but also on subsequent pagination requests.

### Consistency of results

Because pagination forces data streaming over multiple requests, there is a possibility that new data has been added/deleted/modified between the first request and subsequent requests. A pagination implementation SHOULD attempt to maintain the consistency of pagination results to avoid duplication or missed records. If consistency of results is not guaranteed, this MUST be indicated in the standard’s documentation. The ability to provide consistent results will depend on the underlying implementation of a standard.

## Use cases

### Use case: random seeking within a result set

#### Use offset-based pagination

Random-seeking is a functionality normally requested in human interaction interfaces or where more flexibility needs to be afforded to a client. In the first example, consider an interface which displays the results of a search. Using random-seeking allows a client to skip an arbitrary number of pages ahead in the results or configure the number of records displayed per page. By using random-seeking a standard can afford future clients the ability to configure their paging requirements without enforcing a predetermined policy on all clients. It also allows a client to walk back and forth along a result set. Many underlying data querying technologies implement random seeking (e.g. Solr, ElasticSearch, MongoDB) and as such adoption is easy.

### Use case: parallel block retrieval

#### Use offset-based pagination

To speed up results retrieval, a client may wish to split results retrieval into multiple parallel requests. A client can construct URLs representing a block of data to retrieve based on a specified size and offset into the results set. Parameters must be predictable and allow random seeking within a response (see above use-case).

### Use case: streaming large result sets

#### Use offset-based pagination

When encountering the “Deep Paging” issue i.e. where the number of results is a large number, many data querying technologies switch to a token-based system where the last result returned is remembered to ensure pagination consistency and predictability. Results processing is normally a one-way process i.e. you cannot request a prior page.

## Pagination logic

An implementation may choose to drive the pagination logic from a client or from the server, however the server ultimately controls how to paginate through a results set.

### Client side driven logic

Client side driven logic indicates the client itself is responsible for the development of code to paginate. If offset pagination is used the client SHOULD be capable of knowing when results are exhausted and avoiding the need to make additional requests i.e. by providing the total number of known results. If token based pagination is used, the client needs to construct the correct corresponding URL.

See Beacon 2 [BEACON 2] for an example of this pattern. N.B. whilst the Tool Registry Service implements offset-based pagination, it constructs appropriate URLs for the client and therefore encapsulates the logic server side.

### Server side driven logic

Server side driven logic places responsibility for constructing a valid request for the next page of data to a server implementation. If used the client MUST be passed a URL which MAY be fully-resolved or relative to the server [RFC 3986] and when executed will return the next page of data. The links MUST be encoded in the payload (following HATEOAS patterns) to avoid a dependency upon transport protocol. The links MAY be encoded in the underlying protocol transfer headers such as HTTP Headers [RFC 5988], [RFC 8288]. Encoding logic into the server allows a server to control client behaviour explicitly e.g. no longer providing a next URL when the results have been exhausted.

#### Parameters

- **next**: A url representing the next payload of data. MUST be presented. MUST be null if there is no subsequent page
- **last**: A url representing the last payload of data. MAY be presented
- **self**: A url representing the current payload of data. MAY be presented

**Example body payload**

```json
{
  "results" : [
    ...
  ],
  "pagination" : {
    "next" : "/path/query?token=ghi",
    "last" : "/path/query?token=abc",
    "self" : "/path/query?token=def"
  }
}
```

## Considerations

### Existing GA4GH standards implementing pagination

A number of GA4GH standards implement pagination, not limited to TRS, Data Connect and Beacon 2. This recommendation MUST NOT retroactively apply to these standards or subsequent iterations of them. Existing standards MAY adopt the recommendations in this guide but only after consultation and consideration of existing implementations.

## References

[AGENDA] - [GA4GH Connect London 2023 TASC Agenda](https://docs.google.com/document/d/1f3WpLHfJiR2surLAOEuFeyrBllkPHSThvFhHgHcDzCo/edit)

[PRESENTATION] - [GA4GH Connect London 2023 TASC Presentation](https://docs.google.com/presentation/d/1Ceuhx1lpzIbqjPxGpJj2uqlw_BtYJtLM/edit#slide=id.p1)

[TRS] - [https://ga4gh.github.io/tool-registry-service-schemas/](https://ga4gh.github.io/tool-registry-service-schemas/)

[DC] - [https://github.com/ga4gh-discovery/data-connect/blob/develop/SPEC.md](https://github.com/ga4gh-discovery/data-connect/blob/develop/SPEC.md)

[B2] - [https://docs.genomebeacons.org/](https://docs.genomebeacons.org/)

[GITHUB] - [https://docs.github.com/en/rest/guides/using-pagination-in-the-rest-api](https://docs.github.com/en/rest/guides/using-pagination-in-the-rest-api)

[MICROSOFT] - [https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md#98-pagination](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md#98-pagination)

[RFC 3986] - [https://www.rfc-editor.org/rfc/rfc3986#section-4.2](https://www.rfc-editor.org/rfc/rfc3986#section-4.2)

[RFC 5988] - [https://www.rfc-editor.org/rfc/rfc5988#section-5.5](https://www.rfc-editor.org/rfc/rfc5988#section-5.5)

[RFC 8288] - [https://www.rfc-editor.org/rfc/rfc8288#section-3.5](https://www.rfc-editor.org/rfc/rfc8288#section-3.5)
