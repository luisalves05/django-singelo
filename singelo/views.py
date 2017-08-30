from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.
class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, 'singelo/index.html', context)
