from django.db import models

# Create your models here.

#Teacher Model
class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qulification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    skills=models.TextField()
    class Meta:
        verbose_name_plural="1. Teacher"
    

#Course Category  Model
class CourseCategory(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    
    class Meta:
        verbose_name_plural="2. Course Categories"


#Course Model
class Course(models.Model):
    category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    
    class Meta:
        verbose_name_plural="3. Courses"


#Student Model

class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qulification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    address=models.TextField()
    interestred_categories=models.TextField()
    
    class Meta:
        verbose_name_plural="4. Students"