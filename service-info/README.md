# GA4GH Service Info Types

This file details how to add values to the list of Service Info type values for the GA4GH API.

## Background

To enable servers using the suite of GA4GH APIs to be used in a networks, the Service Info endpoint was created. A centrally maintained list of the type values for GA4GH APIs was requested, which was to be managed by the GA4GH TASC Force. See [here for the main Service Info repository](https://github.com/ga4gh-discovery/ga4gh-service-info).

## Using This File

`ga4gh-service-info.json` captures the group and artifact values of the type field. The artifact should be written in kebab case i.e. lower case ASCII character values, with - character as a separator if required.

### JSON format

The JSON file shall feature entries in the following format:
```json
[
  {
    "type": {
      "group": "org.ga4gh",
      "artifact": "first-api-name"
    }
  },
  {
    "type": {
      "group": "org.ga4gh",
      "artifact": "other-api-name"
    }
  }
]
```

## Process

Additional items can be raised as required for standards. It is recommended that this is done in conjunction with the preparation of Product Approval documentation. For further guidelines see [the GA4GH Product Approval Process Guide](https://w3id.org/ga4gh/product-approval).

To add an item to this list, please take the following steps.
<ol>
<li>Create a fork of the TASC repo in your own user space</li>
<li>Modify the JSON file with the values for your PR, keeping the entries ordered alphabetically</li>
<li>Submit the changes as a PR back into the TASC repository</li>
<li>Notify the GA4GH Secretariat or TASC Force directly</li>
<li>The GA4GH TASC Force will review and either approve or comment. Please respond to comments to allow the process to move forwards.</li>
</ol>


