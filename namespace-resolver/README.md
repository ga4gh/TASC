# GA4GH Namespaced Identifier Registration

This file details how to register prefixes and resolution patterns for the `GA4GH` namespace.

## Background

GA4GH standards such as refget and VRS provide methods for the construction of computed identifiers under the GA4GH namespace. These identifiers have type prefixes allowing for sharing of the GA4GH namespace, e.g. `ga4gh:SQ.cQvw4UsHHRRlogxbWCB8W-mKD4AraM9y` representing a refget sequence identifier. To avoid namespace collisions (e.g. another standard using the `SQ` type string), a centralized registry of identifier types and resolution patterns should be managed by TASC. This enables coordination across the GA4GH organization and provides a means for community members seeking to dereference `ga4gh` namespaced identifiers to documentation about what those objects are.

## Using This File

`identifier-prefixes.yaml` captures the identifier name, schema URI, and documentation URI, as applicable.

### YAML format

The YAML file shall feature entries in the following format:
```yaml
prefixes:
  - SQ:
      name: refget sequence
      documentation: https://ga4gh.github.io/refget/sequences/#refget-checksum-algorithm
  - VA:
      name: VRS Allele
      documentation: https://vrs.ga4gh.org/en/stable/concepts/MolecularVariation/Allele.html
      schema: https://w3id.org/ga4gh/schema/vrs/2.0/json/Allele
```

### Type Prefixes

A GA4GH identifier is constructed according to this syntax:

```
"ga4gh" ":" type_prefix "." digest
```

The `digest` is computed as described above. The type_prefix is a short alphanumeric code that corresponds to the type of object being represented.

These are our recommendations for type prefixes:

* Prefixes SHOULD be short, ideally 2-4 characters.
* Characters MUST be uppercase only.
* Prefixes SHOULD be for concrete types, not polymorphic parent classes.
* A prefix MUST map 1:1 with a schema type.

## Process

Additional namespace type prefixes raised as required for standards. It is recommended that this is done in conjunction with the preparation of Product Approval documentation. Prefix requests require the approval of the specification product owners. For further guidelines see [the GA4GH Product Approval Process Guide](https://w3id.org/ga4gh/product-approval).

To add an item to this list, please take the following steps:

- Create a fork of the TASC repo in your own user space</li>
- Modify the YAML file with the values needed for your specification, keeping the entries ordered alphabetically
- Submit the changes as a PR back into the TASC repository
- Notify GA4GH TASC directly
- GA4GH TASC will review and inform on subsequent steps

Items should not be removed from this list, as otherwise eventual new additions may collide with historical values which may be still in use with their original meanings by older servers.
If an item is to be retired or renamed, the existing entry should be retained with two additional fields:

- `status`, which must be one of `"superseded"` or `"withdrawn"`;
- `note`, which is a free-form string describing why the item is no longer active.

## Notes

It is strongly recommended that these prefixes do not change with new versions of the product.
