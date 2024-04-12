from django.db import models


class GymStudent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    heigth = models.DecimalField(max_digits=3, decimal_places=2)
    weigth = models.DecimalField(max_digits=5, decimal_places=2)
