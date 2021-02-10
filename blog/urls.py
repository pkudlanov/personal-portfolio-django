from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>/', views.detail, name='detail'),
]