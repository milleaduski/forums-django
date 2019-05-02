from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
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

class Profile(models.Model):
	user 	= models.OneToOneField(User, on_delete=models.CASCADE)
	activation_key 	= models.CharField(max_length=255, default=1)
	email_validated = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User, dispatch_uid="save_new_user_profile")
def save_profile(sender, instance, created, **kwargs):
	user = instance
	if created:
		profile = Profile(user=user)
		profile.save()