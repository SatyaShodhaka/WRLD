from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path('/',views.view_forum, name='view_form'),
    path('/create-post/',views.create_forum, name='create_forum'),
]