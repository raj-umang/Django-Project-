from django.db import models

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=40)
    course_credits = models.IntegerField()

class Student(models.Model):
    student_usn = models.charField(max_length=20)
    student_name = models.charField(max_length=400)
    student_sem= models.IntegerField()
    enrollment = models.ManyToManyFiels(Course)

