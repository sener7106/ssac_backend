
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser) :
    
    """ Custom USer model """
    
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    
    GENDER_CHOICES = (
        (GENDER_FEMALE , "Female"),
        (GENDER_MALE , "Male")
    )
    
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    
    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN , "Korea"),
        (LANGUAGE_ENGLISH, "English")
    )
    
    
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length = 10, null=True, blank=True)
    

def __str__ (self) :
    return self.name