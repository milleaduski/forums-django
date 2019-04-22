from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('password_change/', views.ChangePassword, name='change-password')
]