# Generated by Django 3.2.20 on 2023-07-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
        ('account', '0002_teachermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='school',
            field=models.ManyToManyField(to='school.SchoolModel'),
        ),
    ]
