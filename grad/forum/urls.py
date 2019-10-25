from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path('',views.view_post, name='view_post'),
    path('create-post/',views.create_post, name='create_post'),
    path('post/<int:id>/',views.full_post,name="post-detail"),
    path('tech/',views.tech_post,name="tech_post"),
    path('music/',views.music_post,name="music_post"),
    path('news/',views.news_post,name="news_post"),
    path('food/',views.food_post,name="food_post"),
    path('entertainment/',views.envi_post,name="envi_post"),
    # path('post/<int:id>/edit')
]