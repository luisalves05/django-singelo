from django.shortcuts import render
from django.core.urlresolvers import resolve

from django.views import View
from .models import Post


class IndexView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts, "app_name": resolve(request.path).app_name}
        return render(request, 'singelo/index.html', context)

class PostView(View):
    def get(self, request, year, month, slug):
        post = Post.objects.get(post_slug = slug)
        context = {"post": post}
        return render(request, 'singelo/post.html', context)
