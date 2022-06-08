from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator

class Userdata(models.Model):
    fname = models.CharField(max_length=50, default="")
    lname = models.CharField(max_length=50, default="")
    Username = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    adress = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    pincode = models.IntegerField(default=000000, validators=[MinValueValidator(6),MaxValueValidator(6)])
    typee = models.CharField(max_length=20, default="Patient")
    image = models.ImageField(upload_to="images/")

    def register(self):
        self.save()

    