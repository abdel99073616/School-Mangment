from django.urls import path , include
from .views import  *
urlpatterns = [
    path('createteacher/' , Teacher_AView , name = 'aa') , 
    path('createparent/' , Parent_AView , name = 'aa') ,
    path('createclassroom/' , Classroom_AView , name = 'aa') ,
    path('createactivites/' , Activites_AView , name = 'aa') ,
    path('createstudent/' , Student_AView , name = 'aa') ,

]
