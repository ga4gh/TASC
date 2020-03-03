# GA4GH Service Info Types

This file details how to add values to the list of Service Info type values for the GA4GH API.

## Background

To enable servers using the suite of GA4GH APIs to be used in a networks, the Service Info endpoint was created. A centrally maintained list of the type values for GA4GH APIs was requested, which was to be managed by the GA4GH TASC Force. See [here for the main Service Info repository](https://github.com/ga4gh-discovery/ga4gh-service-info).

## Using These Files

There are two accompanying files here which should have the same information in both formats.

### JSON format

The JSON file shall features entries in the following format:
```
[
  {
    "type": {
      "group": "org.ga4gh",
      "artifact": "first-api-name",
      "version": "1.0.0"
    }
  },
  {
    "type": {
      "group": "org.ga4gh",
      "artifact": "other-api-name",
      "version": "x.y.z"
    }
  }
]
```

### TSV File

The TSV file will feature tab-separated entries of the format:
```
group   artifact    version
org.ga4gh   first-api-name  1.0.0
org.ga4gh   other-api-name  x.y.z
```


## Process

To add an item to this repository, please take the following steps.
<ol>
<li>Create a fork of the TASC repo in your own user space</li>
<li>Modify the TSV and JSON files with the values for your PR</li>
<li>Submit the changes as a PR back into the TASC repository</li>
<li>The GA4GH TASC Force will review and either approve or comment. Please respond to comments to allow the process to move forwards.</li>
</ol>


