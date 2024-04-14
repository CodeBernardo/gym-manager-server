# Generated by Django 5.0.4 on 2024-04-14 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_remove_exercise_routine'),
        ('routines', '0007_remove_routine_exercises_routine_gym_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='routine',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='routines.routine'),
        ),
    ]