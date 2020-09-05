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
    date_time=models.DateTimeField(auto_now_add=True)
    buyer=models.ForeignKey("registration.user_data", on_delete="DO_NOTHING")
    product=models.ForeignKey("ingridients", on_delete="DO_NOTHING")
    status=models.CharField(default ="pending", max_length=50)
    payment=models.CharField(max_length=50 ,default="pending")
class address(models.Model):
    order=models.ForeignKey("order", on_delete="DO_NOTHING")
    house_num=models.CharField(max_length=50)
    street=models.CharField(max_length=500)
    district = models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
