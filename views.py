from django.shortcuts import render
from .models import *

def list(request):
	posts = Post.objects.all()
	c = {'posts': posts, }
	return render(request, 'posts_list.html', c)


def authors(request):
	authors = Author.objects.all()
	c = {'authors': authors, }
	return render(request, 'authors_list.html', c)
