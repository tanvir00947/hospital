from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(default="avatar.svg", null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    is_doctor = models.BooleanField(default=False)

    
    def __str__(self):
        return self.first_name or f"User {self.id}"
    

    @property
    def imageURL(self):
        try:
            url = self.profile_picture.url
            
        except:
            url = ''
        return url
 