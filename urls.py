from django.conf.urls import include, url
from .views import PostList, PostDetail

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view()),
]