# Generated by Django 5.1.3 on 2024-12-11 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('assigned_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hod.class')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hod.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hod.subject')),
            ],
        ),
    ]
