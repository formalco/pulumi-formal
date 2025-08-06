import pulumi
import pulumi_formal as formal

read_only = formal.Permission('read_only',
    name='logs read-only',
    description='read only permission for logs',
    code=
'''package formal.app

import future.keywords.if
import future.keywords.in

default_app_set := {"Logs"}

# Allow full access to Security Team
allow if {
    "Security Team" in input.user.groups
}
''',
    status='active'
)
config = pulumi.Config()
formal_api_key = config.require("formalApiKey")
