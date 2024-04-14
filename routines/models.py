from django.db import models


class DayOfWeek(models.TextChoices):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class Routine(models.Model):
    day_of_week = models.CharField(max_length=15, choices=DayOfWeek.choices)
    gym_student = models.ForeignKey(
        "gym_students.GymStudent",
        on_delete=models.CASCADE,
        related_name="routines",
        null=True
    )
