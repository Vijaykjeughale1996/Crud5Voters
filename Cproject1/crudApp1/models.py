from django.db import models

# Create your models here.
class voters(models.Model):
    ide = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    add = models.CharField(max_length=200)
