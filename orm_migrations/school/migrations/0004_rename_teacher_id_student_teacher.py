# Generated by Django 4.2.5 on 2023-09-29 08:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0003_rename_teacher_student_teacher_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="teacher_id",
            new_name="teacher",
        ),
    ]
