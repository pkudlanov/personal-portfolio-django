from django.db import models


class Tag(models.Model):
    link = 'Edit'
    name = models.CharField(max_length=255)
    active_popper = models.BooleanField(default=False)
    summary = models.TextField(max_length=320, default='Working on it...')
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE, blank=True, null=True)
    url_post = models.URLField(blank=True)

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
