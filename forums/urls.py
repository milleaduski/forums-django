from django.urls import path
from .views import ForumCreate, ForumListView, ForumUserListView

urlpatterns = [
	path('', ForumListView.as_view(), name='forum-list'),
	path('by/<username>/', ForumUserListView.as_view(), name='forum-by'),
	path('add/', ForumCreate.as_view(), name='forum-add')
]