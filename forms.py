# encoding: utf-8
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='user_mode'), label='Текст')
    filter_horizontal = ('authorized_users', )

    class Meta:
        model = Post
        fields = ['title', 'abstract', 'content', 'tags']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserExtendForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput())

    class Meta:
        model = UserExtend
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Не более 1000 знаков',
                              widget=forms.TextInput(attrs={'placeholder': 'Оставьте свой комментарий'}))
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comment
        exclude = ["post"]

