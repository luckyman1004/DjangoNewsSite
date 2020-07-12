from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.crypto import get_random_string

CATEGORY_CHOICES = (
    ('p','POLITICS'),
    ('y','YOUTH'),
    ('e','ENTERTAINMENT'),
    ('c','COVID-19'),
    ('t','TRENDING'),
    ('r','REVIEWS'),
)

class News(models.Model):
    title = models.CharField(max_length=500)
    short_desc = models.CharField(max_length=1000)
    decription = models.TextField(max_length=10000)
    image = models.ImageField()
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=1 , default=0)
    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(max_length=50,unique=True)

    
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=500)
    image_size_950x280 = models.ImageField()
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.title

class trending_today(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    slug = models.SlugField(max_length=50,unique=True)
    
    def __str__(self):
        return self.title

class top_trending(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.title
