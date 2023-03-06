from django.db import models

# Create your models here.

# ADDRESS table
class ADDRESS(models.Model):
    uid = models.CharField(max_length=10)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    city = models.CharField(max_length=30)
    land_mark = models.CharField(max_length=40)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin_code = models.DecimalField(decimal_places=0, max_digits=6)
    phone = models.CharField(max_length=14)



