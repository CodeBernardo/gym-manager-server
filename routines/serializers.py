from rest_framework import serializers
from exercises.serializers import ExerciseSerializer
from routines.models import DayOfWeek


class RoutineSerializer(serializers.Serializer):
    day_of_week = serializers.ChoiceField(choices=DayOfWeek.choices)
    exercises = ExerciseSerializer(many=True)
