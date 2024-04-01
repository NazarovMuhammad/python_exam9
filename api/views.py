from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import permissions



class CourseListApi(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    
    
class CourseCrateListApi(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    
class CourseUpdeteDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]  
    
    
    
class TeacherCrateListApi(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
    
class TeacherUpdeteDestroyApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]      
    
    

    
          
    
      
    
    
   


    
