from django import forms


from .models import  Teacher_A

class Teacher_AForm(forms.ModelForm):
    class Meta:
        model = Teacher_A
        fields =[
            'Fname' ,
            'Lname' ,
            'address' ,
            'Date_of_Bath' ,
            'password' ,
            'Email' ,
            'last_login',
        ]
   
class RowProdectForm(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    Email = forms.EmailField()
    last_login = forms.DateTimeField()