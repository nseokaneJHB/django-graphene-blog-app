from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


class CustomUserType(DjangoObjectType):
	class Meta:
		model = get_user_model()
		fields = ('id', 'first_name', 'last_name', 'email', 'gender', 'phone_number', 'bio', 'password', 'is_active', 'update_at', 'date_joined', 'slug')