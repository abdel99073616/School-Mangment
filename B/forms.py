from django import forms 

from .models import  Teacher_B ,Parent_B , Classroom_B ,Course_B

class Teacher_BForm(forms.ModelForm):
    class Meta:
        model = Teacher_B
        fields =[
            'Fname' ,
            'Lname' ,
            'address' ,
            'Date_of_Bath' ,
            'password' ,
            'Email' ,
            'last_login',
        ]
   
class RowTeacher_BForm(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    Email = forms.EmailField()
    last_login = forms.DateTimeField()
################################################

class Parent_BForm(forms.ModelForm):
    class Meta:
        model = Parent_B
        fields =[
            'Father_name' ,
            'Mother_name' ,
            'address' ,
            'Phone' ,
            'password' ,
            'last_login',
        ]
   
class RowParent_BForm(forms.Form):
    Father_name =forms.CharField()
    Mother_name = forms.CharField()
    address =  forms.CharField()
    Phone = forms.CharField()
    password = forms.CharField()
    last_login = forms.DateTimeField()

    

###########################################################

class Classroom_BForm(forms.ModelForm):
    class Meta:
        model = Classroom_B
        fields =[
            'Student_Level' ,
            'section' ,
        ]
   
class RowClassroom_BForm(forms.Form):
    Student_Level = forms.CharField()
    section = forms.IntegerField()

#############################################

class Course_BForm(forms.ModelForm):
    class Meta:
        model = Course_B
        fields =[
            'name' ,
        ]
   
class RowCourse_BForm(forms.Form):
    name = forms.CharField()
    

#################################################

