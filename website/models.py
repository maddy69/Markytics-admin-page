from django.db import models

class UserData(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    updated_at = models.CharField(max_length=100)

# Create your models here.
