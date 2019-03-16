from django.urls import path
from .views import ForumCreate

urlpatterns = [
	path('add/', ForumCreate.as_view(), name='forum-add')
]
