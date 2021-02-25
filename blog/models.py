from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
