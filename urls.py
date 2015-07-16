from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='post_list'),
    url(r'^users/$', views.authors, name='post_authors'),
]