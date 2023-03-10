from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

CHARFIELD_MAX_LENGTH=100
CHARFIELD_MIN_LENGTH=50

class Users(AbstractUser):
    USER_ROLE_CHOICES = [
        ("student", "Student"),
        ("staff", "Staff"),
        ("admin", "Admin"),
        ("editor", "Editor")
    ]
    name = models.CharField(max_length=CHARFIELD_MIN_LENGTH, blank=False)
    email = models.EmailField(max_length=CHARFIELD_MAX_LENGTH, blank=False, unique=True)
    role = models.CharField(
        max_length=7, blank=False, choices=USER_ROLE_CHOICES, default="student"
    )
    country = CountryField(blank=False)
    nationality = CountryField(blank=False)
    mobile =  PhoneNumberField(blank=False)