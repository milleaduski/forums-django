from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import SignUpForm
from .token import account_activation_token
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

def SignUp(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user  = form.save()
			user.is_active = False
			user.save()
			token = account_activation_token.make_token(user)
			# Send email
			subject = "Activate your account from email"

			message = render_to_string('activation_email.html',{
					'user' : user,
					'domain' : get_current_site(request).domain,
					'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
					'token' : token
				}
			)
			user.email_user(subject, message)
			return redirect(reverse('home'))
	else:
		form = SignUpForm()

	return render(request, 'signup.html', {'signupForm' : form})

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

def Activate(request):
	return