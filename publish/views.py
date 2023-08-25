from django.shortcuts import render, get_object_or_404
from .models import Post


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.view_count += 1
    post.save()
    return render(request, 'post.html', context={'post': post})
