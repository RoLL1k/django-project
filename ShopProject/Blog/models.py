from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time


def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-' + str(int(time()))


class Post(models.Model):
	title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
	slug = models.SlugField(max_length=150, blank=True, unique=True, verbose_name='Слаг')
	body = models.TextField(blank=True, db_index=True, verbose_name='Пост')
	tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Тэги')
	date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

	class Meta:
		ordering = ['-date_pub']

	def get_absolute_url(self):
		return reverse('post_detail_url', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('post_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('post_delete_url', kwargs={'slug': self.slug})

	def get_comment_url(self):
		return reverse('comment_create_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)
		
	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(max_length=50, verbose_name='Название')
	slug = models.SlugField(max_length=50, blank=True, unique=True, verbose_name='Слаг')

	def get_absolute_url(self):
		return reverse('tag_detail_url', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('tag_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('tag_delete_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title


class Comment(models.Model):
	date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	body = models.TextField(blank=True, db_index=True, verbose_name='Комментарий')
	post = models.ForeignKey('Post', blank=True, related_name='comments', on_delete=models.CASCADE, verbose_name='Пост')

	class Meta:
		ordering = ['-date_pub']

	def __str__(self):
		return self.body[:15]
