from django.urls import path
from .views import ForumCreate, ForumListView

urlpatterns = [
	path('', ForumListView.as_view(), name='forum-list'),
	path('add/', ForumCreate.as_view(), name='forum-add')
]
