from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

#####################################################################

# Teacher Views

def Teacher_AView(request):
    forms = ParentRowForm_A()
    if request.method == "POST" :
        forms = ParentRowForm_A(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Parent_A.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)

#################################################################
# Parent Views


def Parent_AView(request):
    forms = CourseRowForm_A()
    if request.method == "POST" :
        forms = CourseRowForm_A(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Teacher_A.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)

#################################################################

# Classroom Views

def Classroom_AView(request):
    forms = ClassroomRowForm_A()
    if request.method == "POST" :
        forms = ClassroomRowForm_A(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Classroom_A.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)

#################################################################
# Activites Views


def Activites_AView(request):
    forms = ActivitiesRowForm_A()
    if request.method == "POST" :
        forms = ActivitiesRowForm_A(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Activites_A.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)

#################################################################

# Student Views


def Student_AView(request):
    forms = StudentRowForm_A()
    if request.method == "POST" :
        forms = StudentRowForm_A(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Student_A.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)
