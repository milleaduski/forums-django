from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Forum(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Forum, self).save(*args, **kwargs)

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)