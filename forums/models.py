from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

import time

class Forum(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.slug = slugify(self.title) + '-' + time.strftime("%Y%m%d%H%M%S")
		super(Forum, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('forum-list')