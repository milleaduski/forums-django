from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Forum

class ForumCreate(CreateView):
	model = Forum
	fields = ['title','desc']