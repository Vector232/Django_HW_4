# Generated by Django 4.2.5 on 2023-09-29 08:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0005_remove_student_teacher_student_teacher"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="teacher",
            new_name="teachers",
        ),
    ]