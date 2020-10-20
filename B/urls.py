from django.urls import path
from .views import Teacher_BViews , Parent_BViews , Classroom_BViews , Course_BViews
urlpatterns = [
    path('createTeacher_B/' ,Teacher_BViews ,name ='Teacher_B' ),
    path('createParent_B/' ,Parent_BViews ,name ='Parent_B' ),
    path('createClassroom_B/' ,Classroom_BViews ,name ='Classroom_B' ),
    path('createCourse_B/' ,Course_BViews ,name ='Course_B' ),

]

