# Generated by Django 5.0.4 on 2024-04-13 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_students', '0001_initial'),
        ('routines', '0004_alter_routine_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymstudent',
            name='routines',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='routine', to='routines.routine'),
        ),
    ]