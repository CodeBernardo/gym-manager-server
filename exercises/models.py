from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=15)
    number_of_sets = models.IntegerField(default=4)
    number_of_reps_per_set = models.IntegerField(default=12)
    load = models.IntegerField()
    routine = models.ForeignKey(
        "routines.Routine", on_delete=models.CASCADE, related_name="exercise"
    )
