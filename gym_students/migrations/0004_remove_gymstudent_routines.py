# Generated by Django 5.0.4 on 2024-04-14 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_students', '0003_alter_gymstudent_routines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymstudent',
            name='routines',
        ),
    ]
