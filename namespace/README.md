# GA4GH Namespace Register

This file details how and when to add values to the list of GA4GH namespace prefixes for harmonisation across GA4GH APIs, and how the TASC Force will deal with this.

## Background

To enable servers using the suite of GA4GH APIs to be used in a networks, the Service Info endpoint was created. A centrally maintained list of the type values for GA4GH APIs was requested, which was to be managed by the GA4GH TASC Force. See [here for the main Service Info repository](https://github.com/ga4gh-discovery/ga4gh-service-info).

## Using This File

`ga4gh-namespaces.json` captures the fields requested for a namespace request.

The identifier should be written in kebab case i.e. lower case ASCII character values, with - character as a separator if required, and start with 'ga4gh-'.

### JSON format

The JSON file shall feature entries in the following format:
```
[
  {
    "namespace_identifier": {
      "identifier": "",
      "workstream": "",
      "description": "",
    }
  },

]
`
### Example

    "namespace_identifier": {
      "identifier": "",
      "workstream": "",
      "description": "",
    }
  },


## Process

Additional items can be raised as required for standards. 

To add an item to this list, please take the following steps.
<ol>
<li>Create a fork of the TASC repo in your own user space</li>
<li>Modify the JSON file with the values for your PR</li>
<li>Submit the changes as a PR back into the TASC repository</li>
<li>Notify the GA4GH Secretariat or TASC Force directly</li>
<li>The GA4GH TASC Force will circulate amongst themselves, and Work Stream representatives should identify ongoing projects with potential overlaps.</li>
<li>The GA4GH TASC Force will review and either approve or comment. Please respond to comments to allow the process to move forwards.</li>
</ol>



