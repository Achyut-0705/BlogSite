from django.shortcuts import render
from .models import Post

def home(request):
    content = {
        'posts':Post.objects.all(),
        'title':'Blog - Home'        
    }
    return render(request, 'blog/index.html',content)

def about(request):
    return render(request, 'blog/about.html',{'title':'Blog - About'})