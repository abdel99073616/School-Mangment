from django.contrib import admin
from .models import Student_KG ,Student_Course_KG , Activites_KG , Activites_student_teacher_KG , Classroom_KG ,Course_KG , Parent_KG , Sudent_Teacher_KG , Teacher_KG
# Register your models here.


admin.site.register(Student_KG)
admin.site.register(Student_Course_KG)
admin.site.register(Activites_KG)
admin.site.register(Activites_student_teacher_KG)
admin.site.register(Classroom_KG)
admin.site.register(Course_KG)
admin.site.register(Parent_KG)
admin.site.register(Sudent_Teacher_KG)
admin.site.register(Teacher_KG) 