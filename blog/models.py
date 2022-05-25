from django.db import models
from django.contrib.auth.models import User
from portfolio.models import Project
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    active = models.BooleanField(default=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    abstract = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    comment = models.TextField()

    def __str__(self):
        return self.name + ': ' + self.comment[:64] + '...'
