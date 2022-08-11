from django.db import models
from django.contrib.auth.models import User
import os

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique= True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upload_file = models.FileField(upload_to='featured_file/%Y/%m/%d/')  


    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, null= True, blank=True, on_delete=models.SET_NULL)

    tags= models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
