from rest_framework import  serializers
from .models import Students
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=120)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=120)


    def create(self,validate_data):
        return  Students.objects.create(**validate_data)

    