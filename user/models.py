import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users Must Have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

	def AddUser(self, email, password, first_name, last_name, phone_number, roles):
		if password is None:
			raise TypeError('User must have a password')
		user = self.create_user(email ,password)
		user.is_paitent = True
		user.is_active = True
		user.first_name = first_name
		user.last_name = last_name
		user.phone_number = phone_number
		user.roles = roles
		
		user.save()
		return user
		
class User(AbstractBaseUser):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True
	)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	#is_paitent = models.BooleanField(default=False)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	roles = models.IntegerField(default=0)
	phone_number = models.CharField(max_length=15)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()

	def __str__(self):
		return self.email

class Meta:

	db_table = "login"
