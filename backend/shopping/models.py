from django.db import models

# Create your models here.
class ingridients(models.Model):
    name=models.CharField( max_length=150)
    category=models.CharField( max_length=50)
    image=models.CharField( max_length=150 ,null=True)
    price=models.CharField(max_length=50)
    rating=models.CharField( max_length=50)
    description=models.CharField( max_length=500)

class order(models.Model):
    date_time=models.DateTimeField( auto_now=False, auto_now_add=False)
    buyer=models.ForeignKey("registration.user_data", on_delete="DO_NOTHING")
    product=models.ForeignKey("ingridients", on_delete="DO_NOTHING")
