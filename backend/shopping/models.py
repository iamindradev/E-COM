from django.db import models

# Create your models here.
class ingridients(models.Model):
    name=models.CharField( max_length=50)
    category=models.CharField( max_length=50)
    # image=models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    price=models.IntegerField(_(""))
    rating=models.CharField( max_length=50)
    description=models.CharField( max_length=50)

class order(models.Model):
    date_time=models.DateTimeField( auto_now=False, auto_now_add=False)
    buyer=models.ForeignKey("registration.user_data", on_delete="DO_NOTHING")
    
