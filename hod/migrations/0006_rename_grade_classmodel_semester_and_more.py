# Generated by Django 5.1.3 on 2024-12-11 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hod', '0005_alter_classmodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classmodel',
            old_name='grade',
            new_name='semester',
        ),
        migrations.AlterUniqueTogether(
            name='teacherassignment',
            unique_together=set(),
        ),
    ]
