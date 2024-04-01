from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(many=True)
    class Meta:
        model = Course
        fields = ['name_of_curse', 'information', 'teacher']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
