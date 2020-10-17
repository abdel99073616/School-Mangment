from django.db import models
# Create your models here.


class UserAdmin(models.Model):
    FullName = models.CharField(max_length=50)
    Email = models.EmailField()
    password = models.CharField(max_length=20 , null= False)