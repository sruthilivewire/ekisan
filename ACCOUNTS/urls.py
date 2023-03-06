from django.urls import path
from . import views
from KISAN_APP.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('Signup/', views.SignUpPage, name='signup_page'),
    path('SignIn/', views.LoginView, name='login'),
    path('adminHome/', views.adminHome, name='adminHome'),
    path('userHome/', views.userHome, name='userHome'),
    path('staffHome/', views.staffHome, name='staffHome'),
    path('signupView/', views.signupView, name='signupView'),
    path('LogoutView/', views.LogoutView, name='logout'),
    path('Profile/', views.profile, name='profile'),
    path('Profile-Update/', views.profileUpdate, name='update-profile'),
    path('updateMyProfile/', views.updateMyProfile, name='updateMyProfile'),
    ]
