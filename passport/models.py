from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    first_name  = models.CharField(max_length=100)
    second_name  = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    gmc_no  = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    gender = models.BooleanField()
    NI_no =  models.CharField(max_length=100)
    dob     = models.DateField()


class Certificate(models.Model):
    user = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    exp_date=  models.DateField()
    cert_file = models.FileField(upload_to='certificates')

class Address(models.Model):
    user = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    first_line = models.CharField(max_length=100)
    second_line = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)

class HMRCstarter(models.Model):
    user = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    employee_statment = models.CharField(max_length=1, null=True)
    student_loan9 = models.BooleanField(null=True)
    student_loan10 = models.BooleanField(null=True)
    student_loan11 = models.BooleanField(null=True)
    student_loanPlan = models.CharField(max_length=1, null=True)
    postgraduate_loan13 = models.BooleanField(null=True)
    postgraduate_loan14 = models.BooleanField(null=True)
    postgraduate_loan15 = models.BooleanField(null=True)


    