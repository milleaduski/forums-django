from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    # path('password_change/', views.change_password, name='change-password'),
    path('activate/<uidb64>/<token>', views.Activate, name='activate')
]