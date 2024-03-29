# Generated by Django 2.2.12 on 2020-10-15 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activites_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_name', models.CharField(max_length=30)),
                ('Date', models.DateField()),
                ('type_of_activite', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Level', models.CharField(max_length=10)),
                ('section', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parent_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Father_name', models.CharField(max_length=20)),
                ('Mother_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('last_login', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('Date_of_Bath', models.DateField()),
                ('password', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('Class_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='C.Classroom_C')),
                ('parent_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_parent', to='C.Parent_C')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('Date_of_Bath', models.DateField()),
                ('password', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('Email', models.EmailField(max_length=254)),
                ('last_login', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sudent_Teacher_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_Teacher', to='C.Student_C')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to='C.Teacher_C')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Course_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_course', to='C.Course_C')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_Course', to='C.Student_C')),
            ],
        ),
        migrations.CreateModel(
            name='Activites_student_teacher_C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_Teacher_Acivity', to='C.Activites_C')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_Teacher_Acivity', to='C.Student_C')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_teacher_Acivity', to='C.Teacher_C')),
            ],
        ),
    ]
