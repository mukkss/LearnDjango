from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    blog_title = 'Latest Posts'
    posts = [
        {
            'id': 1,
            'title': 'Post 1',
            'content': 'This is the first post'
        },
        {
            'id': 2,
            'title': 'Post 2',
            'content': 'This is the second post'
        },
        {
            'id': 3,
            'title': 'Post 3',
            'content': 'This is the third post'
        },
        {  
            'id': 4,
            'title': 'Post 4',
            'content': 'This is the fourth post'
        },
    ]
    return render(request, 'blog/index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, post_id):
    return render(request, 'blog/details.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse('You are at the new URL')