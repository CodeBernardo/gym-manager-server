from rest_framework import serializers

from routines.serializers import RoutineSerializer


class GymStudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=30)
    date_of_birth = serializers.DateField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)
    heigth = serializers.DecimalField(max_digits=3, decimal_places=2)
    weigth = serializers.DecimalField(max_digits=5, decimal_places=2)
    routines = RoutineSerializer(many=True, read_only=True, allow_null=True, default=None)
