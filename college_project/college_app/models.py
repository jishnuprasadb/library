from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    Course_Name=models.CharField(max_length=70)
    Course_Fee=models.IntegerField()
    
class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    std_name=models.CharField(max_length=100)
    std_age=models.IntegerField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=100)

class Teacher(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        course=models.ForeignKey(Course,on_delete=models.CASCADE)
        phone_number=models.CharField(max_length=100)
        age=models.CharField(max_length=100,null=True)
        photo=models.ImageField(upload_to="image/")
        address=models.TextField(null=True)
