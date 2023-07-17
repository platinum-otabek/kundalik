from rest_framework import serializers
from .models import GradeModel
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeModel
        fields = '__all__'