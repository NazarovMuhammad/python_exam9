from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    pass




class Teacher(models.Model):
    Gander = (
        
    ('MALE','male'),
    ('FEMALE','female'),
    ('NONE','none'),
     )
    
    
    
    full_name = models.CharField( max_length=150)
    email = models.EmailField( max_length=254)
    phone_number = models.CharField(max_length=20)
    gander = models.CharField( max_length=50,choices=Gander)
    
    def __str__(self):
        return self.full_name
    
    


class Course(models.Model):
    name_of_curse = models.CharField( max_length=100)
    information = models.TextField()
    teacher = models.ManyToManyField(Teacher, related_name="Teachers")
    
    def __str__(self):
        return self.name_of_curse
    
    
    
        
    
    