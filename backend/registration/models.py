from django.db import models

# Create your models here.
class user_data(models.Model):
    fname = models.CharField(max_length=50)
    lname= models.CharField(max_length=50 ,null = True) 
    contact = models.CharField(max_length = 150, null = True)
    email = models.EmailField( max_length=254 , null = True)
    e_status= models.CharField( max_length=50 , default="not verified")
    password = models.CharField(max_length=50)


    

    

    