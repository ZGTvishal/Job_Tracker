from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('connect-gmail', views.connect_gmail, name='connect-gmail'),
    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),

]