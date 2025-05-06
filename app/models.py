from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255, unique=True)
    content = RichTextField()
    slug = models.SlugField(default="")
    upload_date = models.DateTimeField(auto_now_add=datetime.now())

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")
    upload_date = models.DateTimeField(auto_now_add=datetime.now())

class Schedule(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.TimeField()
    end_date = models.TimeField()
    event_date = models.DateField()

class Member(models.Model):
    photo = models.ImageField(upload_to="photo/")
    name = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)