from django.db import models

# Create your models here.
class user_data(models.Model):
    fname = models.CharField(max_length=50)
    lname= models.CharField(max_length=50 ,null = True) 
    # contact = models.CharField(max_length = 150, null = True)
    # email = models.EmailField( max_length=254 ,null = True)
    identity = models.CharField(max_length = 150, null = True)
    typ= models.CharField(max_length=50 ,null= True)
    e_status= models.CharField( max_length=50 , default="not verified")
    password = models.CharField(max_length=50)
    otp=models.CharField(max_length=50,null= True)

# class onetimepassword(models.Model):
#     u= models.ForeignKey("user_data",on_delete="DO_NOTHING", null=True)
#     otp= models.CharField(max_length=50)
#     models.DateTimeField( auto_now_add=True)


    

    

    