from rest_framework import serializers
from .models import TeacherModel,StudentModel

# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
    
# class TeacherCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = TeacherModel
#         fields = ['username', 'email', 'password','name','fname',]
    
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'