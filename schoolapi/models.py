from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length = 50)
    s_dob = models.CharField(max_length = 50)
    s_email = models.CharField(max_length = 50)
    s_phone = models.BigIntegerField()
    s_password = models.CharField(max_length = 50)