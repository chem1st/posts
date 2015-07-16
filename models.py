#coding: UTF-8
from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
	user = models.OneToOneField(User, verbose_name='Логин')
	organization = models.CharField(u'Организация', max_length=100)

	def __unicode__(self):
		return unicode(self.user)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Post(models.Model):
	title = models.CharField(u'Заголовок поста', max_length=300)
	datetime = models.DateTimeField(u'Дата публикации')
	author = models.ForeignKey(Author)
	content = models.TextField()

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
