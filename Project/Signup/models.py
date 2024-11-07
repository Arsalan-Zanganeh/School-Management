from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.exceptions import ValidationError
import re

class User(AbstractUser):
    SchoolType = [
        ('boy', 'Boy'),
        ('girl', 'Girl'),
    ]

    EducationLevel = [
        ('elementary', 'Elementary'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
    ]
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=11)
    School_Name = models.CharField(max_length=60)
    Province = models.CharField(max_length=40)
    City = models.CharField(max_length=40)
    Address = models.CharField(max_length=100)
    School_Type = models.CharField(max_length=4, choices=SchoolType, blank=False)
    Education_Level = models.CharField(max_length=10, choices=EducationLevel, blank=False)
    National_ID = models.CharField(max_length=10)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    image = models.ImageField(default='default.jpg', upload_to='user_images')
    verified = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def post_save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(post_save_profile, sender=User)
