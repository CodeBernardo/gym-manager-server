# Generated by Django 5.0.4 on 2024-04-13 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_remove_exercise_routine'),
        ('routines', '0004_alter_routine_day_of_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='gym_student',
        ),
        migrations.AlterField(
            model_name='routine',
            name='exercises',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='exercises.exercise'),
        ),
    ]
