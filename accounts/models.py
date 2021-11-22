from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Use Manager Model Here.
class CustomUserManager(BaseUserManager):

	def _create_user(self, email, password=None, **extra_fields):
		# Create and save user with the given email and password
		if not email:
			raise ValueError('The given email must be set')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		# Handle none superuser
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)


	def create_superuser(self, email, password=None, **extra_fields):
		# Handle none superuser
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


# User Model Here.
class CustomUser(AbstractUser):
	GENDER = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Other', 'Other'),
	)

	username = None
	email = models.EmailField(_('Email Address'), unique=True)
	gender = models.CharField(_('Gender'), max_length=7, choices=GENDER, blank=True)
	phone_number = models.CharField(_('Phone Number'), max_length=9, blank=True)
	bio = models.TextField(_('About Me'), blank=True)
	update_at = models.DateTimeField(_('Update At'), auto_now=True)
	slug = models.SlugField(max_length=255, unique=True,  blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(f'{self.first_name} {self.last_name} {str(self.pk)}')
		super().save(*args, **kwargs)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

