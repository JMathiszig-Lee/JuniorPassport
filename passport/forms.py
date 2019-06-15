from django import forms
from . import models

class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['name', 'speciality', 'gmc_no', 'email']
