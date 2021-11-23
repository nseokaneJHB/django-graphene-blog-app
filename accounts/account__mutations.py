import graphene

from .types import CustomUserType
from django.contrib.auth import get_user_model


class AccountMutation(graphene.Mutation):
	user = graphene.Field(CustomUserType)

	class Arguments:
		phone_number = graphene.String()
		first_name = graphene.String(required=True)
		last_name = graphene.String(required=True)
		password = graphene.String(required=True)
		gender = graphene.String()
		email = graphene.String(required=True)
		slug = graphene.String()
		bio = graphene.String()

	@classmethod
	def mutate(cls, root, info, **kwargs):
		user = get_user_model()(
			first_name = kwargs.get('first_name'),
			last_name = kwargs.get('last_name'),
			gender = kwargs.get('gender') if kwargs.get('gender') is not None else "Not Specified",
			email = kwargs.get('email'),
		)

		user.set_password(kwargs.get('password')),
		user.save()
		return AccountMutation(user=user)