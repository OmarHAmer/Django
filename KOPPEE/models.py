from distutils.command.upload import upload
import email
from email.mime import image
from operator import mod
from pyexpat import model
from turtle import title
from unicodedata import category, name
from venv import create
from django.db import models
from django.utils.text import slugify
# Create your models here.

def upload_image(instance,image):
    imagename , imageexc = image.split('.')
    return 'Image/{}.{}'.format(instance.id,imageexc)

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
    image = models.ImageField(upload_to=upload_image)
    slug = models.SlugField(null=True,blank=True)

    def save (self,*args,**Kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**Kwargs)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name