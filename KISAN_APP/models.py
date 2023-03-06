from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Krishibhavan details

class KRISHIBHAVAN(models.Model):
    uid = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    place = models.CharField(max_length=30)
    municipality = models.CharField(max_length=40)
    panchayath = models.CharField(max_length=40)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pin_code = models.DecimalField(decimal_places=0, max_digits=6)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    ecode = models.CharField(max_length=8)

# online services

class ONLINE_SERVICES(models.Model):
    ecode = models.CharField(max_length=8)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    ServiceName = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Scheme = models.CharField(max_length=200)
    Eligibility = models.CharField(max_length=200)
    How_To_Apply = models.CharField(max_length=200)
    Whom_To_Contact = models.CharField(max_length=200)
    URL = models.CharField(max_length=200)
    Last_Date = models.DateField()


# table for applications of user
class SCHEME_APPLICATIONS(models.Model):
    uid = models.CharField(max_length=8)
    Name = models.CharField(max_length=40)
    Aadhar_No = models.CharField(max_length=12)
    Email = models.EmailField()
    Phone = models.CharField(max_length=14)
    Village = models.CharField(max_length=40)
    Panchayath = models.CharField(max_length=40)
    District = models.CharField(max_length=40)
    pin_code = models.IntegerField()
    is_KisanCard = models.IntegerField()
    Scheme_id = models.CharField(max_length=10)

# table for user side notifications

class USER_NOTIFICATIONS(models.Model):
    text = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.text



