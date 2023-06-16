from django.db import models

# Create your models here.
class Teacher(models.Model):
    Teacher_id=models.CharField(max_length=100)
    Teacher_Name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Teacher_id
class Courses(models.Model):
    Teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Course_id=models.CharField(max_length=100)
    Course_Name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Course_Name
