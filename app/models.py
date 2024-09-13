from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.

class Blogs(models.Model):
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255, unique=True)
    content = RichTextField()
    upload_date = models.DateTimeField(auto_now_add=datetime.now())

class Registration(models.Model):
    pass