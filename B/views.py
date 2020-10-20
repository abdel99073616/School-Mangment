from django.shortcuts import render
from .forms import RowTeacher_BForm , RowParent_BForm ,RowClassroom_BForm , RowCourse_BForm 
from .models import  Teacher_B ,Parent_B , Classroom_B ,Course_B


def Teacher_BViews(request):
    forms = RowTeacher_BForm()
    if request.method == "POST" :
        forms = RowTeacher_BForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Teacher_B.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)
##############################################################
def Parent_BViews(request):
    forms = RowParent_BForm()
    if request.method == "POST" :
        forms = RowParent_BForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Parent_B.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)

#####################################################

def Classroom_BViews(request):
    forms = RowClassroom_BForm()
    if request.method == "POST" :
        forms = RowClassroom_BForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Classroom_B.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)
    #######################################################
def Course_BViews(request):
    forms = RowCourse_BForm()
    if request.method == "POST" :
        forms = RowCourse_BForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Course_B.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)