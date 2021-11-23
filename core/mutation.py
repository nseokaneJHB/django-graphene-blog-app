import graphene

# Account
from accounts.account__mutations import AccountMutation

# Authentication
import graphql_jwt


class Mutation(graphene.ObjectType):
	create_account = AccountMutation.Field()
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()