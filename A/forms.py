from django import forms
from .models import  Student_A ,Student_Course_A , Activites_A , Activites_student_teacher_A , Classroom_A ,Course_A , Parent_A , Sudent_Teacher_A , Teacher_A


#################################################################################
# Teacher Form

class TeacherForm_A(forms.ModelForm):
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
   
class TeacherProdectForm_A(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    Email = forms.EmailField()
    last_login = forms.DateTimeField()

#################################################################################

# Parent Form

class ParentForm_A(forms.ModelForm):
    class Meta:
        model = Student_A
        fields =[
            'Father_name' ,
            'Mother_name' ,
            'address' ,
            'phone' ,
            'password' ,
            'last_login',
        ]
   
class ParentProdectForm_A(forms.Form):
    Father_name = forms.CharField()
    Mother_name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    password = forms.CharField()
    last_login = forms.DateTimeField()

###############################################################################
# Course Form

class CourseForm_A(forms.ModelForm):
    class Meta:
        model = Course_A
        fields =[
            'name' 
        ]
   
class CourseProdectForm_A(forms.Form):
    name = forms.CharField()

#################################################################################

# Student Form

class ClassroomForm_A(forms.ModelForm):
    class Meta:
        model = Student_A
        fields =[
            'Fname' ,
            'Lname' ,
   
class StudentProdectForm_A(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    Email = forms.EmailField()
    last_login = forms.DateTimeField()

#################################################################################

# Student Form

class StudentForm_A(forms.ModelForm):
    class Meta:
        model = Student_A
        fields =[
            'Fname' ,
            'Lname' ,
            'address' ,
            'Date_of_Bath' ,
            'password' ,
            'Email' ,
            'last_login',
        ]
   
class StudentProdectForm_A(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    Email = forms.EmailField()
    last_login = forms.DateTimeField()


#################################################################################


# Student Form

class StudentForm_A(forms.ModelForm):
    class Meta:
        model = Student_A
        fields =[
            'Fname' ,
            'Lname' ,
            'address' ,
            'Date_of_Bath' ,
            'password' ,
            'Email' ,
            'last_login',
        ]
   
class StudentProdectForm_A(forms.Form):
    Fname = forms.CharField()
    Lname = forms.CharField()
    address = forms.CharField()
    Date_of_Bath = forms.DateField()
    password = forms.CharField()
    Email = forms.EmailField()
    last_login = forms.DateTimeField()


