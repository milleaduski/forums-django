from django.urls import path
from . import views

urlpattern = [
    path('signup/', views.SignUp.as_view(), name=sigup),
]
