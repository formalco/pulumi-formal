import * as pulumi from "@pulumi/pulumi";
import * as formal from "@formalco/pulumi";

const read_only = new formal.Permission('read_only', {
    name: 'logs read-only',
    description: 'read only permission for logs',
    code:
`package formal.app

import future.keywords.if
import future.keywords.in

default_app_set := {"Logs"}

# Allow full access to Security Team
allow if {
    "Security Team" in input.user.groups
}
`,
    status: 'draft'
})