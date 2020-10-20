from django.urls import path , include
from .views import  *
urlpatterns = [
    path('createteacher/' , Teacher_AView , name = 'a1') , 
    path('createparent/' , Parent_AView , name = '2') ,
    path('createclassroom/' , Classroom_AView , name = '3') ,
    path('createactivites/' , Activites_AView , name = '4') ,
    path('createstudent/' , Student_AView , name = '5') ,

]
