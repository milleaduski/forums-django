from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Forum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')

class ForumListView(ListView):
	model = Forum
	#context_object_name  = "objForums"
	queryset = Forum.objects.order_by('-created_at')

class ForumUserListView(ListView):
	template_name = 'forums/forum_by_user.html'
	def get_queryset(self):
		self.user = get_object_or_404(User, username = self.kwargs['username'])
		return Forum.objects.filter(user = self.user)

class ForumDetailView(DetailView):
	model = Forum
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['additional'] = ''
		return context

class ForumUpdateView(UpdateView):
	model = Forum
	fields = ['title','desc']
	template_name = 'forums/forum_update_form.html'



class ForumCreate(CreateView):
	model = Forum
	fields = ['title','desc']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)