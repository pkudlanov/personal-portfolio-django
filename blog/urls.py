from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.AllPosts.as_view(), name='all_posts'),
    path('<slug:slug>/', views.DetailPost.as_view(), name='detail'),
]