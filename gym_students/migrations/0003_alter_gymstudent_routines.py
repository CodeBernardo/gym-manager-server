# Generated by Django 5.0.4 on 2024-04-14 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_students', '0002_gymstudent_routines'),
        ('routines', '0005_remove_routine_gym_student_alter_routine_exercises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymstudent',
            name='routines',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='routines', to='routines.routine'),
        ),
    ]
