# Generated by Django 5.1.3 on 2024-12-11 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hod', '0003_classmodel_remove_subject_assigned_class_and_more'),
        ('teacher', '0002_alter_quiz_assigned_class_alter_quiz_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
