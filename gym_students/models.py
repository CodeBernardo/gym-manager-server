from django.db import models


class GymStudent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    heigth = models.DecimalField(max_digits=3, decimal_places=2)
    weigth = models.DecimalField(max_digits=5, decimal_places=2)


# student_1 = {
#     "first_name": "Bernardo",
#     "last_name": "Stein",
#     "date_of_birth": "1993-01-23",
#     "email": "bernardo@mail.com",
#     "password": "123456",
#     "heigth": 1.74,
#     "weigth": 83.70,
# }
