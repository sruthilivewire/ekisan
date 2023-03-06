from django.urls import path
from . import views
from ACCOUNTS.views import *
urlpatterns = [

    # common access
    path('', views.index, name='index'),
    path('About Us/', views.AboutUs, name='about_us'),
    path('Services/', views.Services, name='services'),
    path('Schemes/', views.Schemes, name='schemes'),
    path('Administration/', views.Administration_Details, name='administration'),
    path('Contact Us/', views.ContactUs, name='contact'),

    # admin module

    path('Privacy Policy/', views.PrivacyPolicy, name='privacy_policy'),
    path('krishibhavanlist/', views.krishibhavanList, name='krishibhavanlist'),
    path('addKrishibhavan/', views.addKrishibhavan, name='addKrishibhavan'),
    path('e-Registration/', views.KrishibhavanRegistration, name='e_reg'),
    path('More-Details/<int:id>', views.KrishibhavanMoreDetails, name='KrishibhavanMoreDetails'),
    path('Krishibhavan-update/<int:id>', views.updateKrishibhavan, name='Krishibhavan-update'),
    path('Krishibhavan-delete/<int:id>', views.Krishibhavan_delete, name='Krishibhavan-delete'),

    # staff module

    path('Online-Services/', views.OnlineServices, name='OnlineServices'),
    path('Add-Online-Services/', views.AddOnlineServices, name='addOnlineServices'),
    path('New-Services/', views.Add_NewOnlineServices, name='addNewOnlineServices'),
    path('readMore_OnlineServices/<int:id>', views.readMore_OnlineServices, name='readMore_OnlineServices'),
    path('deleteOnlineServices/<int:id>', views.deleteOnlineServices, name='deleteOnlineServices'),

    # user module

    path('user_SchemeDetails/', views.user_SchemeDetails, name='user_SchemeDetails'),
    path('readMore_OnlineServices_user/<int:id>', views.readMore_OnlineServices_user, name='readMore_OnlineServices_user'),
    path('Apply_Services_User/<int:id>', views.Apply_Services_User, name='Apply_Services_User'),
    path('Scheme_Application_Submit', views.Scheme_Application_Submit, name='Scheme_Application_Submit'),
    path('User_Notifications/', views.User_Notifications, name='User_Notifications'),
    path('make_as_read/<int:id>/', views.MarkasRead, name='MarkasRead'),
    path('User_KrishibhavanList/', views.User_KrishibhavanList, name='User_KrishibhavanList'),
    path('KisanCard/', views.KisanCard, name='KisanCard'),
    path('KisanCardForm/', views.KisanCardForm, name='KisanCardForm'),
    path('KisanCardApply/', views.KisanCardApply, name='KisanCardApply'),


]
