from rest_framework import serializers
from .models import TeacherModel,StudentModel,CustomUser

from django.contrib.auth import get_user_model

User = get_user_model()

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
    
class TeacherCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = TeacherModel
        fields = ['username', 'password', 'name', 'fname', 'subject', 'toifa', 'salary', 'school', 'date_of_birth']
   
    def create(self, validated_data):
        
        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
        }

        user = CustomUser.objects.create_user(**user_data)
        school = validated_data.pop('school')
        teacher = TeacherModel.objects.create(user=user, school=school, **validated_data)
        return teacher
    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'