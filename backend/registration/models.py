from django.db import models

# Create your models here.
class user_data(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length = 150)
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=50)

    

    

    