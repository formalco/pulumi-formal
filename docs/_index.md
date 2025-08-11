---
# *** WARNING: This file was auto-generated. Do not edit by hand unless you're certain you know what you are doing! ***
title: Formal Provider
meta_desc: Provides an overview on how to configure the Pulumi Formal provider.
layout: package
---

## Installation

The Formal provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@pulumi/formal`](https://www.npmjs.com/package/@pulumi/formal)
* Python: [`pulumi-formal`](https://pypi.org/project/pulumi-formal/)
* Go: [`github.com/formalco/pulumi-formal/sdk/go/formal`](https://github.com/pulumi/pulumi-formal)

## Overview

Use the Formal Pulumi Provider to interact with the
many resources supported by Formal.

Use the navigation to the left to read about the available resources.
## Authentication and Configuration

Configuration for the Formal Provider is derived from the API tokens you can generate via the Formal Console.
### Provider Configuration

!> **Warning:** Hard-coded credentials are not recommended in any Pulumi
configuration and risks secret leakage should this file ever be committed to a
public version control system.

Credentials can be provided by adding an `apiKey`.

Usage:

```yaml
# Pulumi.yaml provider configuration file
name: configuration-example
runtime:
config:
    formal:apiKey:
        value: 'TODO: var.formal_api_key'
    formal:retrieveSensitiveValues:
        value: true

```

Credentials can be provided by using the `FORMAL_API_KEY` environment variables.

For example:

Usage:

```yaml
# Pulumi.yaml provider configuration file
name: configuration-example
runtime:

```

```bash
export FORMAL_API_KEY="some_api_key"
```
#### Retrieving Sensitive Values

You can configure the Formal Provider to disabled retrieving sensitive values from the Formal API. This is useful for resources such as `formalControlPlaneTlsCertificate` and `machineRoleAccessToken` where the sensitive values are returned by default. To enable this feature, set the `retrieveSensitiveValues` parameter to `false`.
### Deploying with a Managed Cloud model

Registering resources such as Keys and Datastores under the Managed Cloud model require the `cloudAccountId` parameter, which is the Formal ID of your cloud integration. You can find this information in the "Integrations" side panel in the Formal Console.
## Examples

See examples for each resource in the `examples/` folder.