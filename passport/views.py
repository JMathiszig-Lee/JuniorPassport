from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from . import forms
from . import models

def index(request):
    return HttpResponse("Hello, world.")


def new_doctor(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.DoctorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/viewdoctors')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.DoctorForm()
        return render(request, 'adddoctor.html', {'form': form})

class ViewDoctors(ListView):
    model = models.Doctor

def show_documents(request, gmc_no):
    current_doctor = models.Doctor.objects.get(gmc_no=gmc_no)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.DocumentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # instance = forms.DocumentForm(file_field=request.FILES['file'])
            # instance.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/documents/' + str(gmc_no))
        else: 
            print(form._errors)
            form = forms.DocumentForm(initial={'user':current_doctor.name})
            return render(request, 'documents.html', {'form': form, 'doctor': current_doctor})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.DocumentForm(initial={'user':current_doctor.name})
        return render(request, 'documents.html', {'form': form, 'doctor': current_doctor})