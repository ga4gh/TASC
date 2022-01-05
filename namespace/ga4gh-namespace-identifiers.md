# GA4GH Namespace Identifiers

This document outlines the cross-workstream, GA4GH-wide namespace identifier system. Identifiers under the `ga4gh` namespace are compact uniform resource identifiers (CURIEs) that unambiguously associate the object at the given id with the data model (outlined in a GA4GH specification) it is constructed according to.

## Background

The GA4GH mission entails structuring, connecting, and sharing data reliably. A key component of this effort is to be able to `identify` entities, that is, to associate identifiers with entities. Ideally, there will be exactly one identifier for each entity, and one entity for each identifier. Traditionally, identifiers are assigned to entities, which means that disconnected groups must coordinate on identifier assignment.

The computed identifier scheme proposed in the Variation Representation Specification (VRS) computes identifiers from the data itself. Because identifiers depend on the data, groups that independently generate the same variation will generate the same computed identifier for that entity, thereby obviating centralized identifier systems and enabling identifiers to be used in isolated settings such as clinical labs.

The computed identifier mechanism is broadly applicable and useful to the entire GA4GH ecosystem. Adopting a common identifier scheme will make interoperability of GA4GH entities more obvious to consumers, will enable the entire organization to share common entity definitions (such as sequence identifiers), and will enable all GA4GH products to share tooling that manipulate identified data. In short, it provides an important consistency within the GA4GH ecosystem.

## Background

The following algorithmic processes, described in depth in VRS [Computed Identifiers](https://vrs.ga4gh.org/en/1.0/impl-guide/computed_identifiers.html#computed-identifiers), are included in this proposal by reference:

* **GA4GH Digest Serialization** is the process of converting an object to a canonical binary form based on JSON and inspired by similar (but unratified) JSON standards. This serialization for is used only for the purposes of computing a digest.

* **GA4GH Truncated Digest** is a convention for using [SHA-512](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf), truncated to 24 bytes, and encoding using [base64url](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

* **GA4GH Identification** is the CURIE-based syntax for constructing a namespaced and typed identifier for an object.

## Type Prefixes

![GA4GH type prefixes](./img/type-prefixes.png)

A GA4GH identifier is constructed according to this syntax:

```
"ga4gh" ":" type_prefix ":" digest
```

The `digest` is computed as described above. The type_prefix is a short alphanumeric code that corresponds to the type of object being represented.

These are our recommendations for type prefixes:

* Prefixes SHOULD be short, ideally 2-4 characters.
* Prefixes SHOULD be for concrete types, not polymorphic parent classes.
* A prefix MUST map 1:1 with a schema type.

See the [type prefix registry](./type-prefix-registry.md) for the current list of approved type prefixes under the `ga4gh` namespace.

## Type Prefix Submission Process

All GA4GH work streams are encouraged to use existing type prefixes in their specifications wherever possible, and to submit new type prefixes for data models that aren't currently represented in the registry.

To add an entry to the type prefix registry:
* Fork the TASC repository in your own user space
* In your user space, create a new branch from `ga4gh:master`
* In the new branch, add an additional row in the markdown table in `type-prefix-registry.md` with your proposed type prefix.
* Create a Pull Request (PR) to the `ga4gh:master` branch
* TASC will review the proposed type prefix and comment and/or request modifications on the PR thread.
* TASC will merge the PR once all comments have been addressed
