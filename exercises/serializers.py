from rest_framework import serializers


class ExerciseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)
    number_of_sets = serializers.IntegerField(default=4)
    number_of_reps_per_set = serializers.IntegerField(default=12)
    load = serializers.IntegerField()


# exercise1 = {
#     "name": "Rosca direta",
#     "number_of_sets": 4,
#     "number_of_reps_per_set": 12,
#     "load": 20,
# }

# exercise2 = {
#     "name": "Rosca punho",
#     "number_of_sets": 4,
#     "number_of_reps_per_set": 15,
#     "load": 12,
# }
