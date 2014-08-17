from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

# # Create your models here.
# class  Users(models.Model):
# 	name = models.CharField(max_length=100, null=True, blank=True)
# 	email = models.EmailField(max_length=100, null=True, blank=True)
# 	password = models.CharField(max_length=8, null=True, blank=True)

# 	def save(self):
# 		user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


# 	class Meta:
# 		app_label = 'users_manage'

class MyUserManager(BaseUserManager):
	def create_user(self, email, date_of_birth, password=None):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, date_of_birth, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(email,
			password=password,
			
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	# On Python 3: def __str__(self):
	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin



