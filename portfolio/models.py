from django.db import models
from blog.models import Category


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    tags = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.title
