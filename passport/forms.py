from django import forms
from . import models

class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['name', 'speciality', 'gmc_no', 'email']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Certificate
        fields = '__all__' 
        widgets = {
            'exp_date': forms.widgets.SelectDateWidget()
        }