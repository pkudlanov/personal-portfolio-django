from django.db import models
# from blog.models import Category


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=320)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url_production = models.URLField(blank=True)
    url_blogpost = models.URLField(blank=True)
    url_github = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self) -> str:
        return self.title
