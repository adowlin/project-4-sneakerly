from django.shortcuts import render


def blog(request):
    """ View to show & post blog submissions """
    context = {}
    return render(request, 'blog/blog.html', context)
