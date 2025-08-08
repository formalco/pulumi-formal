# Permissions example

To run this example, you will need to specify a Formal API key. You can do this in two ways:

1. Use the pulumi config variable `formal:apiKey`:
```
pulumi config set formal:apiKey MY_API_KEY
```
2. Use the environment variable `FORMAL_API_KEY`:
```
FORMAL_API_KEY=MY_API_KEY pulumi up
```

Then simply run `pulumi up` to add the permission resource to Formal.