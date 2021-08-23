from django.shortcuts import render

from .forms import BlogPostForm


def blog(request):
    """ View to show blog posts """
    context = {}
    return render(request, 'blog/blog.html', context)


def add_blog_post(request):
    """ View to add a blog post """
    form = BlogPostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/add_blog_post.html', context)
