from django.contrib.auth.models import User

class Doctor(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    gmc_no  = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)


class Certificate(models.Model):
    user = models.ForeignKey(doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    exp_date=  model.DateTimeField()
    cert_file = models.FileField(upload_to='certifcates')
