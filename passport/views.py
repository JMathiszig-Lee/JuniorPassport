from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import forms

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
