from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path('',views.view_post, name='view_post'),
    path('create-post/',views.create_post, name='create_post'),
]