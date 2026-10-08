# GA4GH Group Acronyms

This file details how to register new group acronyms

## Background

The [Citing GA4GH Documentation](../../recommendations/Citing%20GA4GH%20Documentation.md) requires the use of a known group acronym to create the `<std_designator>` metadata item. Contained in this directory is the registry of `<ORIGINATING_GROUP_ACRONYM>`. This is need is established in ADR [TASC-ADR-004](../../adr/TASC-ADR-004%20Use%20Standard%20Designators%20for%20DOI%20Metadata.md).

Only the acronyms found here will be used/

## Process

Creating an acronym follows this process:

  1. Establish your group does not have an acronym by [referring to the registry file](originating-group-acronyms.yaml)
  2. Fork this repository and in your fork add the acronym to the `originating-group-acronyms.yaml` file
  3. Keep entries alphabetical by acronym and never remove an entry
  4. Renamed or retired groups are kept with a `status: superseded` tag and a `note` explaining the change
  5. Open a PR against this repo and it will be merged

## TASC Responsibilities

TASC will ensure this list is correctly maintained. 

## Technical Team Responsibilities

Technical team will ensure only the acronyms listed here will be used to create `<std_designator>` items.
