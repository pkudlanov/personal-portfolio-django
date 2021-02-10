from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    body = models.TextField(max_length=555)

    def __str__(self) -> str:
        return self.title
