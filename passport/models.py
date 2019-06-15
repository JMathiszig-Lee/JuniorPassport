from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name  = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    gmc_no  = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    user = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    exp_date=  models.DateField()
    cert_file = models.FileField(upload_to='certificates')
