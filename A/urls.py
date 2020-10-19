from django.urls import path , include
from .views import  prodect
urlpatterns = [
    path('create/' , prodect , name = 'aa')
]
