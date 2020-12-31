from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + " by " + self.author
class Post1(models.Model):
    sno1=models.AutoField(primary_key=True)
    title1=models.CharField(max_length=255)
    author1=models.CharField(max_length=14)
    slug1=models.CharField(max_length=130)
    timeStamp1=models.DateTimeField(blank=True)
    content1=RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title1 + " by " + self.author1

class Post2(models.Model):
    sno2=models.AutoField(primary_key=True)
    title2=models.CharField(max_length=255)
    author2=models.CharField(max_length=14)
    slug2=models.CharField(max_length=130)
    timeStamp2=models.DateTimeField(blank=True)
    content2=RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title2 + " by " + self.author2
