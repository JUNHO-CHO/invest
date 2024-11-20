from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
	GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

	username = models.CharField(max_length=15, unique=True)
	nickname = models.CharField(max_length=10, unique=True)
	name = models.CharField(max_length=10)
	birthday = models.DateField()
	gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
	email = models.EmailField(unique=True, blank=True)
	phone_number = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'010-?[0-9]{3}-?[0-9]{4}', 'Invalid phone number format')])
	address = models.CharField(max_length=100)
	profile_image = models.ImageField(upload_to='profile_images/', blank=True)
	bio = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username

#  조준호 뭐먹으러감 조주노 왔따~