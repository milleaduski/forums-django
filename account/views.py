from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import SignUpForm
from .token import account_activation_token
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
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
					'uid' : urlsafe_base64_encode(force_bytes(user.pk)).decode(),
					'token' : token
				}
			)
			user.email_user(subject, message)
			return redirect(reverse('home'))
	else:
		form = SignUpForm()

	return render(request, 'signup.html', {'signupForm' : form})

# def ChangePassword(request):
# 	if request.method == 'POST':
# 		form = PasswordChangeForm(request.user, request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			update_session_auth_hash(request, user)
# 			return redirect(reverse('home'))
# 	else:
# 		form = PasswordChangeForm(request.user)
# 	return render(request, 'change_password.html', {'form' : form})
## OLD password: newadmin1994
## New password: admin1994

def Activate(request, uidb64, token):
	uid = force_text(urlsafe_base64_decode(uidb64).decode())
	user = User.objects.get(pk=uid)

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_validated = True
		user.save()
		return redirect(reverse('home'))
