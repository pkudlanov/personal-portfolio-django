from django.db import models
from django.contrib.auth.models import User
from portfolio.models import Project


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    abstract = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
