from django import forms
from . import models

class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Certificate
        fields = '__all__' 
        widgets = {
            'exp_date': forms.widgets.SelectDateWidget()
        }

class StarterFrom(forms.ModelForm):
    class Meta:
        model = models.HMRCstarter
        fields = '__all__'
