import pulumi_formal as formal

owner='mokhtar@joinformal.com'

decrypt = formal.Policy('decrypt',
    name='decrypt',
    description='decrypt any columns that has the name encrypted-col.',
    owner=owner,
    notification='none',
    status='active',
    module='''package formal.v2

import future.keywords.if
import future.keywords.in

post_request := { "action": "decrypt", "columns": columns } if {
    columns := [col | col := input.row[_]; col["name"] == "encrypted-col"]
}
'''
)

mask_emails = formal.Policy('mask_emails',
    name='mask-email',
    description='Mask any column that has the data label email_address.',
    owner=owner,
    notification='consumer',
    status='active',
    module='''
package formal.v2

import future.keywords.if

post_request := { "action": "mask", "type": "redact.partial", "sub_type": "email_mask_username", "columns": columns, "typesafe": "fallback_to_default" } if {
    columns := [col | col := input.columns[_]; col["data_label"] == "email_address"]
}
'''
)

row_level_hashing = formal.Policy('row_level_hashing',
    name='test-row-level-hashing-eu',
    description='hash every row that has the eu column set to true.',
    owner=owner,
    notification='all',
    status='active',
    module='''package formal.v2

import future.keywords.if

post_request := { "action": "mask", "type": "hash.with_salt", "columns": input.columns } if {
    colValue := [col | col := input.row[_]; col["name"] == "eu"; col["value"] == true]
    count(colValue) > 0
}
'''
)

block_db_with_formal_message = formal.Policy('block_db_with_formal_message',
    name='block_db_with_formal_message',
    description='this policy block connection to sidecar based on the name of db and drop the connection with a formal message',
    owner=owner,
    notification='all',
    status='active',
    module='''package formal.v2

import future.keywords.if
import future.keywords.in

default session := { "action": "block", "type": "block_with_formal_message" }

session := { "action": "allow", "reason": "the policy is blocking request" } if {
    input.db_name == "main"
    "USAnalyst" in input.user.groups
    input.datastore.technology == "postgres"
}
'''
)

http_pre_request_name_hash = formal.Policy('http_pre_request_name_hash',
    name='http_pre_request_name_hash',
    description='this policy hash every names in body request of HTTP requests',
    owner=owner,
    notification='all',
    status='active',
    module='''package formal.v2

import future.keywords.if

pre_request := { "action": "mask", "type": "hash.with_salt", "columns": columns } if {
    columns := [col | col := input.row[_]; col["data_label"] == "name"]
}
'''
)