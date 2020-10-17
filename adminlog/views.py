from django.shortcuts import render
from .models import UserAdmin
# Create your views here.



def AdminView_register(reqest):
    if reqest.method == 'POST':
        FName = reqest.POST.get('fullname_register')
        Email = reqest.POST.get('email_register')
        password = reqest.POST.get('pass_register')

        informations = UserAdmin(
            FullName = FName ,
            Email = Email ,
            password = password
        )
        informations.save()
    return render (reqest , 'register.html')
    
