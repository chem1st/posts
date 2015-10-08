from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^$', PostListView.as_view(),
        name='posts'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TaggedPostListView.as_view(),
        name='tagged'),
    url(r'^new/$', login_required(PostCreateView.as_view(
        template_name='posts/post_form.html')),
        name='post_new'),
    url(r'^update/(?P<slug>[-\w]+)/$', login_required(PostUpdateView.as_view(
        template_name='posts/post_form.html')),
        name='post_update'),
    url(r'^delete/(?P<slug>[-\w]+)/$', login_required(PostDeleteView.as_view(
        template_name='posts/post_confirm_delete.html')),
        name='post_delete'),
    url(r'^profile/$', login_required(ProfileView.as_view(
        template_name='posts/profile.html')),
        name='profile'),
    url(r'^profile/update/$', login_required(profile_update),
        name='profile_update'),
    url(r'^profile/posts$', login_required(ProfilePostListView.as_view(
        template_name='posts/user_post_list.html')),
        name='my_posts'),
    url(r'^profile/comments$', login_required(ProfileCommentListView.as_view(
        template_name='posts/user_comment_list.html')),
        name='my_comments'),
    url(r'^users/(?P<pk>[\d]+)/$', UserDetailView.as_view(
        template_name='posts/user_info.html'),
        name='user'),
    url(r'^(?P<slug>[-\w]+)/add_comment/$', add_comment,
        name='add_comment'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(),
        name='post_detail'),
]