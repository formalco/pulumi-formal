package main

import (
	formal "github.com/formalco/pulumi-formal/sdk/go/formal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		provider, err := formal.NewProvider(ctx, "provider", &formal.ProviderArgs{
			ApiKey: pulumi.String("APIKEY"),
		})
		if err != nil {
			return err
		}
		p := pulumi.Provider(provider)

		list, err := formal.NewConnectorListener(ctx, "postgres_pl_listener", &formal.ConnectorListenerArgs{
			Name: pulumi.StringPtr("postgres-pl-listener"),
			Port: pulumi.Int(10446),
		}, p)
		if err != nil {
			return err
		}
		ctx.Export("postgres-pl-listener", list)

		psql, err := formal.NewResource(ctx, "postgres-pl", &formal.ResourceArgs{
			Name:       pulumi.StringPtr("postgres-pl"),
			Hostname:   pulumi.String("localhost"),
			Technology: pulumi.String("postgres"),
			Port:       pulumi.Int(10447),
		}, p)
		if err != nil {
			return err
		}
		ctx.Export("postgres-pl", psql)

		user, err := formal.NewNativeUser(ctx, "postgres-pl-user", &formal.NativeUserArgs{
			ResourceId:       psql.ID(),
			NativeUserId:     pulumi.String("postgres"),
			NativeUserSecret: pulumi.String("postgres"),
		}, p)
		if err != nil {
			return err
		}
		ctx.Export("postgres-pl-user", user)

		return nil
	})
}
