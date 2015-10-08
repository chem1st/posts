#encoding: UTF-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from unidecode import unidecode


class UserExtend(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Логин')
    town = models.CharField(u'Город', max_length=100, blank=True)
    age = models.IntegerField(u'Возраст', blank=True)
    organization = models.CharField(u'Организация', max_length=100, blank=True)
    tel = models.CharField(u'Телефон', max_length=15, blank=True)

    def __unicode__(self):
        return unicode(self.user)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_absolute_url(self):
        return "/posts/authors/%i/" % self.id


class Post(models.Model):
    title = models.CharField(u'Заголовок', max_length=300)
    slug = models.SlugField(u"URL", default='')
    created = models.DateTimeField(u'Дата публикации', auto_now_add=True)
    modified = models.DateTimeField(u'Дата изменения', auto_now=True)
    author = models.ForeignKey(User, verbose_name=u'Автор', blank=True)
    abstract = models.TextField(u'Краткое содержание (макс. 1000 знаков)', max_length=1000)
    content = RichTextField(u'Текст')
    tags = TaggableManager(help_text="""Вводите теги через запятую.
        Теги могут состоять из нескольких слов. Например: гималайская соль, портал, дровяная печь, канадский кедр.""")
    activity = models.BooleanField(u"Активность", default=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-modified']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='comment_created')
    author = models.ForeignKey(User, blank=True, null=True)
    content = models.TextField(max_length=1000)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.content[:60]))

    class Meta:
        ordering = ['-created']
