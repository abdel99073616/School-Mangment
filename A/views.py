from django.shortcuts import render
from .forms import RowProdectForm
from .models import Teacher_A
# Create your views here.


def prodect(request):
    forms = RowProdectForm()
    if request.method == "POST" :
        forms = RowProdectForm(request.POST)
        if forms.is_valid():
            print(forms.cleaned_data)
            Teacher_A.objects.create(**forms.cleaned_data)
        else:
            print(forms.errors)
    context = {
        "form" : forms
    }

    return render(request , "form.html" , context)