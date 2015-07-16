from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
#custom project settings
from cms.models import *


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    #custom project settings
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.get(activity=True)
        context['tels'] = context['contacts'].tel.all()
        context['bg'] = Background.objects.get(activity=True)
        return context

class PostDetail(DetailView):
    model = Post
