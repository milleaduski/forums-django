from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Forum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')

class ForumListView(ListView):
	model = Forum
	context_object_name  = "objForums"
	queryset = Forum.objects.order_by('created_at')

	# queryset = Forum.objects.order_by('created_at','desc')

class ForumCreate(CreateView):
	model = Forum
	fields = ['title','desc']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)