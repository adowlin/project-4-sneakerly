from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path(
        'edit/<int:blog_post_id>/',
        views.edit_blog_post, name='edit_blog_post'),
    path(
        'delete/<int:blog_post_id>/',
        views.delete_blog_post, name='delete_blog_post'),
]
