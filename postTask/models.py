from django.db import models
# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return str(self.title)


class Skill_Task(models.Model):
    Skill_title= models.CharField(max_length=100)
    Task_title= models.CharField(max_length=100)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    skills = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    publishdate = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)