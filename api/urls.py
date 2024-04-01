from django.urls import path
from .views import *





urlpatterns = [
    path("",CourseListApi.as_view()),
    path('crate-course/',CourseCrateListApi.as_view()),
    path('update-course/<int:pk>/',CourseUpdeteDestroyApi.as_view()), 
    path('crate-teacher/',TeacherCrateListApi.as_view()),
    path('update-teacher/<int:pk>/',TeacherUpdeteDestroyApi.as_view()), 
]

