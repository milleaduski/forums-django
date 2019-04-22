from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import SignUpForm

def SignUp(request):
	# success_url = reverse_lazy('login')
	# template_name = 'signup.html'
	formClass = SignUpForm
	return render(request, 'signup.html', {'signupForm' : formClass})

def ChangePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect(reverse('home'))
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'change_password.html', {'form' : form})
## OLD password: newadmin1994
## New password: admin1994