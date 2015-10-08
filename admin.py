#encoding: UTF-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class HideAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class PostAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'author', 'activity']
    list_filter = ['author']


class UserExtendInline(admin.StackedInline):
    model = UserExtend


class UserAdmin(UserAdmin):
    inlines = (UserExtendInline, )


class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author"]
    list_filter = ['post', 'author']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserExtend, HideAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
