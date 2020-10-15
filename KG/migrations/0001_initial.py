# Generated by Django 2.2.12 on 2020-10-15 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activites_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_name', models.CharField(max_length=30)),
                ('Date', models.DateField()),
                ('type_of_activite', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Level', models.CharField(max_length=10)),
                ('section', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parent_KG',
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
            name='Student_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('Date_of_Bath', models.DateField()),
                ('password', models.CharField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('Class_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='KG.Classroom_KG')),
                ('parent_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_parent', to='KG.Parent_KG')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_KG',
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
            name='Sudent_Teacher_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_Teacher', to='KG.Student_KG')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to='KG.Teacher_KG')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Course_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_course', to='KG.Course_KG')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_Course', to='KG.Student_KG')),
            ],
        ),
        migrations.CreateModel(
            name='Activites_student_teacher_KG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_Teacher_Acivity', to='KG.Activites_KG')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_Teacher_Acivity', to='KG.Student_KG')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student_teacher_Acivity', to='KG.Teacher_KG')),
            ],
        ),
    ]
