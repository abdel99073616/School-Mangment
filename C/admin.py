from django.contrib import admin
from .models import Student_C ,Student_Course_C , Activites_C , Activites_student_teacher_C , Classroom_C ,Course_C , Parent_C , Sudent_Teacher_C , Teacher_C
# Register your models here.


admin.site.register(Student_C)
admin.site.register(Student_Course_C)
admin.site.register(Activites_C)
admin.site.register(Activites_student_teacher_C)
admin.site.register(Classroom_C)
admin.site.register(Course_C)
admin.site.register(Parent_C)
admin.site.register(Sudent_Teacher_C)
admin.site.register(Teacher_C)