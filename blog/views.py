from django.shortcuts import render
from django.contrib import messages

from .forms import BlogPostForm


def blog(request):
    """ View to show blog posts """
    context = {}
    return render(request, 'blog/blog.html', context)


def add_blog_post(request):
    """ View to add a blog post """
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your photo has been added!')
            render(request, 'blog/blog.html')
        else:
            messages.error(request, 'Failed to add photo. Please make sure the form is valid.')
    else:
        form = BlogPostForm()

    context = {
        'form': form
    }
    return render(request, 'blog/add_blog_post.html', context)
