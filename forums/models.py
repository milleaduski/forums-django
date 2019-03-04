from django.db import models
from django.conf import settings

class Forum(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)