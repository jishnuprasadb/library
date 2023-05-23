import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class StudentRegistration(models.Model):
    student_name=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    email=models.EmailField()
    address=models.TextField()
    