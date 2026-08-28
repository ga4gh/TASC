# Service Info Type Registry Guide

**Source**: TASC  
**Recommendation**: GA4GH-REC-02  
**Title**: Service Info Type Registry Guide  
**Related GitHub issues**: [#1](https://github.com/ga4gh/TASC/issues/1), [#16](https://github.com/ga4gh/TASC/issues/16), [#67](https://github.com/ga4gh/TASC/issues/67)  
**Raised by**: Melissa Konopko (Technical Team)  
**Authors**: Jeremy Adams, John Marshall, Mamana Mbiyavanga  
**Date:** 2025-01-28  
**Status:** Approved  
**Keywords**: service-info, registry, discovery, naming  
**Work Streams Impacted**: All work streams  
**Products Affected**: All GA4GH API products  

## Abstract

This recommendation defines the governance, structure, and lifecycle management of the GA4GH Service Info Type Registry, which maintains a centralized registry of standardized service type identifiers for GA4GH API servers. The registry enables service discovery within GA4GH networks by providing a consistent naming system using a two-part identifier structure (group and artifact). This document describes the process for registering new service types, the required naming conventions, lifecycle management of registry entries, and guidance for implementers. The recommendation establishes TASC as the governing body for registry additions and defines processes that ensure backward compatibility and prevent identifier collisions.

## Table of contents

- [Recommendation](#recommendation)
- [Background](#background)
- [Detailed Guidance](#detailed-guidance)
  - [Service type structure](#service-type-structure)
  - [Registration process](#registration-process)
  - [Registry entry format](#registry-entry-format)
  - [Lifecycle management](#lifecycle-management)
  - [Implementation guidance](#implementation-guidance)
  - [Security considerations](#security-considerations)
- [Use Cases](#use-cases)
  - [Use case - service discovery in networks](#use-case---service-discovery-in-networks)
  - [Use case - capability negotiation](#use-case---capability-negotiation)
  - [Use case - monitoring and observability](#use-case---monitoring-and-observability)
- [Considerations](#considerations)
  - [Existing GA4GH products](#existing-ga4gh-products)
  - [Non-GA4GH service types](#non-ga4gh-service-types)
- [References](#references)
- [Contributors](#contributors)

## Recommendation

GA4GH services MUST register their service type identifiers in the centralized Service Info Type Registry maintained by TASC. Service types MUST use the standardized two-part naming structure consisting of a group identifier (typically "org.ga4gh") and an artifact identifier in kebab-case format. New service type registrations MUST follow the submission and review process defined in this document. Registry entries MUST NOT be deleted; deprecated entries SHOULD be marked with appropriate status annotations. Implementations MUST expose their service type information through the Service Info endpoint as defined in the GA4GH Service Info specification. This recommendation applies to new GA4GH products and existing products MAY adopt it through coordination with TASC.

## Background

The Service Info Type Registry provides a centralized, authoritative source of standardized identifiers that enable GA4GH API servers to declare their capabilities in a machine-readable format. This allows clients, network operators, and monitoring tools to discover available services without manual configuration or documentation lookups. By maintaining a single registry, GA4GH ensures consistency across implementations, prevents identifier collisions, and provides a clear governance process for adding new service types. The registry supports network-level orchestration, automated service discovery, capability negotiation, and monitoring of GA4GH service ecosystems. It serves as the foundation for building federated networks of GA4GH services that can interoperate seamlessly.

## Detailed Guidance

### Service type structure

#### Group identifier

The group identifier represents the organization or namespace that defines and maintains the service type. For GA4GH standardized services, the group identifier MUST be "org.ga4gh". Organizations implementing custom extensions or non-standard services MAY use their own group identifier following reverse domain notation (e.g., "org.example" for example.org).

#### Artifact identifier

The artifact identifier specifies the particular API or service type within the group namespace. Artifact identifiers MUST use kebab-case formatting: lowercase letters and numbers separated by hyphens. The artifact name SHOULD be concise, descriptive, and reflect the service's primary function. For versioned APIs, the version MAY be included in the artifact identifier (e.g., "beacon-v2") or handled through separate versioning fields.

#### Naming constraints

Artifact identifiers MUST conform to the following regular expression pattern:

```text
^([a-z][a-z0-9]*)(-[a-z0-9]+)*$
```

This pattern enforces:
- Must start with a lowercase letter
- May contain lowercase letters and digits
- May include hyphens as separators (but not at the start or end)
- No uppercase letters, underscores, or special characters

Valid examples: `tool-registry-service`, `beacon-v2`, `drs`
Invalid examples: `ToolRegistry`, `beacon_v2`, `DRS`, `-service`

### Registration process

#### Submitting new service types

Product developers MUST submit new service type registrations through GitHub pull requests to the TASC repository. The submission process is:

1. Fork the GA4GH TASC repository
2. Modify the `service-info/ga4gh-service-info.json` file to add the new entry
3. Maintain alphabetical ordering of entries by artifact identifier
4. Submit a pull request with a clear description of the service type
5. Notify the GA4GH Secretariat or TASC Force via appropriate communication channels

Submitters SHOULD provide context about the service's purpose, its relationship to existing GA4GH standards, and expected adoption timeline.

#### Review and approval workflow

TASC reviews service type registration requests during regular meetings or asynchronously through GitHub. The review process evaluates:

- Naming compliance with registry conventions
- Uniqueness and lack of collision with existing identifiers
- Alignment with GA4GH principles and standards
- Completeness and clarity of submission

TASC MAY request revisions, suggest alternative naming, or require additional documentation. Contributors MUST respond to review feedback to advance the registration. Approvals are documented through pull request merge and recorded in TASC meeting minutes.

#### Coordination with product approval

Service type registration SHOULD be coordinated with the GA4GH product approval process. Products undergoing standards approval SHOULD submit service type registrations early in the approval cycle to ensure consistency between the service type identifier and the final product specification. For products already approved, service type registration MAY occur retrospectively but SHOULD reference the approved product specification.

### Registry entry format

#### Required fields

Each registry entry MUST include:

- **type**: An object containing:
  - **group**: The group identifier (typically "org.ga4gh")
  - **artifact**: The artifact identifier in kebab-case

```json
{
  "type": {
    "group": "org.ga4gh",
    "artifact": "service-name"
  }
}
```

#### Optional fields

Entries MAY include additional metadata:

- **version**: The API version string if not encoded in the artifact identifier
- **status**: Lifecycle status ("active", "superseded", "withdrawn")
- **note**: Human-readable description or deprecation notice
- **superseded_by**: Reference to the replacement service type (for deprecated entries)
- **documentation_url**: Link to official service documentation

```json
{
  "type": {
    "group": "org.ga4gh",
    "artifact": "old-service"
  },
  "status": "superseded",
  "note": "Replaced by new-service v2.0",
  "superseded_by": {
    "group": "org.ga4gh",
    "artifact": "new-service"
  }
}
```

#### Example entries

Active service type:

```json
{
  "type": {
    "group": "org.ga4gh",
    "artifact": "tool-registry-service"
  }
}
```

Deprecated service type:

```json
{
  "type": {
    "group": "org.ga4gh",
    "artifact": "legacy-api"
  },
  "status": "withdrawn",
  "note": "Service discontinued as of 2024-06-01"
}
```

### Lifecycle management

#### Active entries

Active service types represent currently supported GA4GH APIs. These entries remain in the registry indefinitely and serve as the authoritative reference for implementers. Updates to active entries SHOULD be minimal and limited to adding optional metadata fields. Changes to the core type identifiers (group and artifact) MUST NOT occur once an entry is registered.

#### Deprecated entries

When a service type is superseded or withdrawn, the entry MUST remain in the registry with appropriate status annotations. This preserves the historical record and prevents identifier reuse that could cause confusion. Deprecated entries MUST include:

- A **status** field set to "superseded" or "withdrawn"
- A **note** field explaining the deprecation reason
- For superseded services, a **superseded_by** reference to the replacement

Servers implementing deprecated service types SHOULD continue to report them in their Service Info responses to maintain backward compatibility with older clients.

#### Versioning considerations

Service type identifiers MAY encode version information in the artifact name (e.g., "beacon-v2") or through separate version fields. When major API revisions occur that break backward compatibility, implementers SHOULD register a new service type entry rather than modifying the existing one. This allows servers to explicitly signal which API versions they support and enables clients to make informed compatibility decisions.

### Implementation guidance

#### Server implementation

Servers MUST implement the GA4GH Service Info endpoint as defined in the Service Info specification. The endpoint MUST return a JSON response containing the service type information from the registry. Minimal implementation:

```json
{
  "id": "org.example.server-001",
  "name": "Example GA4GH Server",
  "type": {
    "group": "org.ga4gh",
    "artifact": "tool-registry-service"
  },
  "organization": {
    "name": "Example Organization"
  },
  "version": "1.0.0"
}
```

Servers implementing multiple GA4GH APIs MAY report multiple service types through additional fields or repeated type entries, depending on the Service Info specification version.

#### Client discovery

Clients SHOULD query the Service Info endpoint to determine server capabilities before making API requests. This enables:

- Automatic detection of supported API versions
- Graceful degradation when servers don't support expected features
- Dynamic routing in federated networks
- Capability-based service selection

Clients SHOULD NOT hardcode assumptions about server capabilities and SHOULD handle unknown service types gracefully.

#### Multi-service servers

Servers hosting multiple GA4GH APIs SHOULD expose multiple Service Info endpoints (one per service) or include multiple service type declarations in a single response. The implementation approach depends on the server architecture and Service Info specification version. Implementers SHOULD clearly document how clients can discover all available services on a multi-service server.

### Security considerations

Service Info endpoints typically do not require authentication as they provide public metadata about service capabilities. However, implementers SHOULD consider:

- **Rate limiting**: Prevent abuse of discovery endpoints
- **Information disclosure**: Avoid exposing sensitive internal details in service descriptions
- **Version information**: Consider security implications of advertising specific software versions
- **Registry integrity**: TASC MUST ensure the registry itself is protected from unauthorized modifications

Implementers MAY choose to require authentication for Service Info endpoints in security-sensitive environments, but this may limit discoverability.

## Use Cases

### Use case - service discovery in networks

**Scenario**: A client needs to locate DRS (Data Repository Service) servers within a federated GA4GH network.

**Solution**: The client queries known network nodes for their Service Info endpoints, filters responses by service type `{"group": "org.ga4gh", "artifact": "drs"}`, and identifies available DRS servers without manual configuration.

**Benefits**: Automatic service discovery, reduced configuration burden, dynamic network adaptation.

### Use case - capability negotiation

**Scenario**: A workflow engine needs to determine if a server supports specific GA4GH APIs before submitting jobs.

**Solution**: The engine queries the server's Service Info endpoint, checks for the required service types (e.g., TES, WES), and validates version compatibility before proceeding.

**Benefits**: Prevents runtime failures, enables graceful degradation, supports multi-version environments.

### Use case - monitoring and observability

**Scenario**: A network operator needs to monitor the health and availability of GA4GH services across multiple institutions.

**Solution**: Monitoring tools periodically query Service Info endpoints across the network, track service availability, detect version changes, and alert on inconsistencies or outages.

**Benefits**: Proactive issue detection, network-wide visibility, compliance verification.

## Considerations

### Existing GA4GH products

Existing GA4GH products that pre-date this recommendation MAY have already established service type identifiers outside the registry. These products SHOULD register their identifiers retrospectively to ensure completeness of the registry. Identifiers used in production deployments MUST be preserved to maintain backward compatibility, even if they don't fully conform to current naming conventions. TASC MAY grant exceptions for established identifiers on a case-by-case basis.

### Non-GA4GH service types

Organizations implementing GA4GH APIs alongside proprietary or non-standard services MAY use custom group identifiers outside the "org.ga4gh" namespace. The registry maintained by TASC is authoritative only for "org.ga4gh" service types. Organizations maintaining custom registries SHOULD follow similar governance practices to prevent confusion and identifier collisions within their own ecosystems.

## References

- [SERVICE-INFO-SPEC] GA4GH Service Info Specification: https://github.com/ga4gh-discovery/ga4gh-service-info
- [TASC-REGISTRY] GA4GH Service Info Type Registry: https://github.com/ga4gh/TASC/tree/main/service-info
- [PRODUCT-APPROVAL] GA4GH Product Approval Process: https://www.ga4gh.org/how-we-work/approval-process/
- [RFC-3986] URI Generic Syntax: https://www.rfc-editor.org/rfc/rfc3986
- [KEBAB-CASE] Naming Convention Best Practices: https://en.wikipedia.org/wiki/Letter_case#Kebab_case

## Contributors

Contributions are matched against [CRediT](https://credit.niso.org/) taxonomy roles. Organisation affiliations are not currently recorded for these contributors.

| Name | Organisation |
|------|-------------|
| Mamana Mbiyavanga | — |
| Technical Alignment Sub Committee (TASC) | — |

CRediT roles: Mamana Mbiyavanga (Writing – original draft, Writing – review & editing); Technical Alignment Sub Committee (TASC) (Investigation, Writing – review & editing).
