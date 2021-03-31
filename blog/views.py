from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class AllPosts(generic.ListView):
    model = Post
    ordering = ['-id']


class DetailPost(generic.DetailView):
    model = Post
