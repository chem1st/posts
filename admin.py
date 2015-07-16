#coding: UTF-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class AuthorInline(admin.StackedInline):
    model = Author


class UserAdmin(UserAdmin):
    inlines = (AuthorInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Author)
admin.site.register(Post)
