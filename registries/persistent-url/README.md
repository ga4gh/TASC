# GA4GH Persistent URL Redirects

This file details how to register prefixes and resolution patterns for the `GA4GH` namespace.

## Background

Consistency in the structure of pURLs drives consistency and cohesion across products, and makes it easier to document and describe GA4GH schema resources at a high level. GA4GH already uses w3id.org as a persistent URL resolver for GA4GH products. The need for persistent URLs is important for use of online JSON Schema documents that should be resolvable by an $id attribute.

## Persistent URL patterns

Currently, TASC requires persistent URL patterns related to schemas to use the following syntax:

![TASC Schema pURL Syntax](https://github.com/ga4gh/TASC/assets/811065/084da959-cc84-4af9-8184-4063c0e47569)

## Process

Creating or editing a persistent URL redirect rule requires taking the following actions:

  1. Ensure that your persistent URL pattern meets the above criteria
  2. Ensure that your redirect rules point to the correct location
  3. Fork the [ga4gh w3id.org](https://github.com/ga4gh/w3id.org) repository
  4. Create a Pull Request adding your redirect rule(s) to the [.htaccess file](https://github.com/ga4gh/w3id.org/blob/master/ga4gh/.htaccess)
  5. GA4GH TASC will review and inform on subsequent steps, including squash merge and PRs to the upstream w3id.org repo

## TASC Responsibilities

TASC will maintain a regular sync interval with the upstream w3id.org repository.
