from django.db import models

from products.models import Product
from profiles.models import UserProfile


class BlogPost(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='blog_posts')
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='product')
    title = models.CharField(max_length=200)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(default='')

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='blog_comments')
    post = models.ForeignKey(
        BlogPost, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='blog_post')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    comment = models.TextField(default=None, blank=True, null=True)
