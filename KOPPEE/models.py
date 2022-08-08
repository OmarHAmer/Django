from operator import mod
from pyexpat import model
from turtle import title
from unicodedata import category, name
from django.db import models

# Create your models here.


class Job(models.Model):
    JOB_TYPE = (('F','Full Time'),('P','Part Time'),)
    title = models.CharField(max_length=20,blank=False,null=False)
    job_type = models.CharField(max_length=20,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField()
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name