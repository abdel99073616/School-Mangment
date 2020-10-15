# Create your models here.
from django.db import models
from forall.models import Levels
# Create your models here.
class Teacher_B(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    Date_of_Bath = models.DateField()
    password = models.CharField(max_length=20,unique=True)
    image = models.ImageField()
    Email = models.EmailField()
    last_login = models.DateTimeField()

class Parent_B(models.Model):
    Father_name = models.CharField(max_length=20)
    Mother_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    Phone = models.CharField(max_length=11)
    password = models.CharField(max_length=20,unique=True)
    image = models.ImageField()
    last_login = models.DateTimeField()

class Classroom_B(models.Model):
    Student_Level = models.CharField(max_length=10)
    section = models.IntegerField()

class Course_B(models.Model):
    name = models.CharField(max_length=50)

class Activites_B(models.Model):
    act_name = models.CharField(max_length=30)
    Date = models.DateField() 
    type_of_activite = models.CharField(max_length=20)

class Student_B(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    Date_of_Bath = models.DateField()
    password = models.CharField(max_length=20,unique=True)
    image = models.ImageField()
    parent_ID = models.ForeignKey(Parent_B , related_name='student_parent' , on_delete = models.CASCADE )
    Class_ID = models.ForeignKey(Classroom_B , related_name='student_class' , on_delete = models.CASCADE )
    level_ID = models.ForeignKey(Levels , related_name='student_level_B' , on_delete = models.CASCADE)

class Student_Course_B(models.Model):
    student_id = models.ForeignKey(Student_B , related_name='Student_Course' , on_delete = models.CASCADE )
    course_id = models.ForeignKey(Course_B , related_name='Student_course' , on_delete = models.CASCADE )

class Sudent_Teacher_B(models.Model):
    student_id = models.ForeignKey(Student_B , related_name='Student_Teacher' , on_delete = models.CASCADE )
    teacher_id = models.ForeignKey(Teacher_B , related_name='student_teacher' , on_delete = models.CASCADE )


class Activites_student_teacher_B(models.Model):
    student_id = models.ForeignKey(Student_B , related_name='Student_Teacher_Acivity' , on_delete = models.CASCADE )
    teacher_id = models.ForeignKey(Teacher_B , related_name='Student_teacher_Acivity' , on_delete = models.CASCADE )
    activity_id = models.ForeignKey(Activites_B , related_name='student_Teacher_Acivity' , on_delete = models.CASCADE )
