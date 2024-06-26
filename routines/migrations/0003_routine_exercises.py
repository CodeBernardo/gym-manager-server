# Generated by Django 5.0.4 on 2024-04-13 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_remove_exercise_routine'),
        ('routines', '0002_alter_routine_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='exercises',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to='exercises.exercise'),
        ),
    ]
