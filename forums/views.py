from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Forum, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class ForumListView(ListView):
	model = Forum
	queryset = Forum.objects.order_by('-created_at')
	paginate_by = 2

class ForumUserListView(ListView):
	template_name = 'forums/forum_by_user.html'
	def get_queryset(self):
		self.user = get_object_or_404(User, username = self.kwargs['username'])
		return Forum.objects.filter(user = self.user)

class ForumDetailView(DetailView):
	model = Forum
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form_comment'] = CommentForm()
		return context

class OwnerProtectMixin(object):
	def dispatch(self, request, *args, **kwargs):
		objectUser = self.get_object()
		if objectUser.user != self.request.user:
			return HttpResponseForbidden()
		return super(OwnerProtectMixin, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ForumUpdateView(OwnerProtectMixin, UpdateView):
	model = Forum
	fields = ['title','desc']
	template_name = 'forums/forum_update_form.html'

	def get_success_url(self, **kwargs):
		return reverse_lazy('forum-detail', kwargs={'slug' : self.object.slug})


@method_decorator(login_required, name='dispatch')
class ForumDeleteView(SuccessMessageMixin, OwnerProtectMixin, DeleteView):
	model = Forum
	success_url = '/forum'
	success_message = 'Forum was successfully deleted'

@method_decorator(login_required, name='dispatch')
class ForumCreate(SuccessMessageMixin, CreateView):
	model = Forum
	fields = ['title','desc']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class CommentCreateView(CreateView):
	model = Comment
	fields = ['desc']
	success_message = 'Forum was successfully created'

	def form_valid(self, form):
		_forum = get_object_or_404(Forum, id=self.kwargs['pk'])
		form.instance.user = self.request.user
		form.instance.forum = _forum
		return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CommentUpdateView(OwnerProtectMixin, UpdateView):
	model = Comment
	fields = ['desc']
	template_name = 'forums/forum_update_comment.html'

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(OwnerProtectMixin, DeleteView):
	model = Comment
	success_url = '/forum'