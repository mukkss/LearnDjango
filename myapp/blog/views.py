from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    blog_title = 'Latest Posts'
    return render(request, 'blog/index.html', {'blog_title': blog_title})

def detail(request, post_id):
    return render(request, 'blog/details.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse('You are at the new URL')