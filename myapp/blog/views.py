from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import  logging
from .models import Post
from django.http import Http404

# # Create your views here.
#Static demo data 
# posts = [
#     {
#         'id': 1,
#         'title': 'Post 1',
#         'content': 'This is the first post'
#     },
#     {
#         'id': 2,
#         'title': 'Post 2',
#         'content': 'This is the second post'
#     },
#     {
#         'id': 3,
#         'title': 'Post 3',
#         'content': 'This is the third post'
#     },
#     {  
#         'id': 4,
#         'title': 'Post 4',
#         'content': 'This is the fourth post'
#     },
# ]

def index(request):
    blog_title = 'Latest Posts'
    # getting data from post model
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'blog_title': blog_title, 'posts': posts})

def detail(request, slug):
    # getting Static Data
    # post = next((item for item in posts if item['id'] == int(post_id)), None)
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist!")

    #   Getting data from model using ID
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post variable is {post}')
    return render(request, 'blog/details.html', {'post' : post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse('You are at the new URL')