from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import BlogPost
from .forms import BlogPostForm


def blog(request):
    """ View to show blog posts """
    blog_posts = BlogPost.objects.all()
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog/blog.html', context)


def add_blog_post(request):
    """ View to add a blog post """
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been added!')
            render(request, 'blog/blog.html')
        else:
            messages.error(
                request, 'Failed to add photo. \
                    Please make sure the form is valid.')
    else:
        form = BlogPostForm()

    context = {
        'form': form
    }
    return render(request, 'blog/add_blog_post.html', context)


def edit_blog_post(request, blog_post_id):
    """ Edit a blog post """

    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('blog'))
        else:
            messages.error(
                request, 'Failed to update post. \
                    Please ensure the form is valid.')
    else:
        form = BlogPostForm(instance=blog_post)

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


def delete_blog_post(request, blog_post_id):
    """Delete a blog post"""
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    blog_post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
