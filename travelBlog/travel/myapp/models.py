from django.db import models
# Create your models here.
class UserData(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=100)
    description=models.CharField(max_length=255)


