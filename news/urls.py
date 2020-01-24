from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name ='screen-home'),
   path('profile/', views.profile, name='user-profile'),
   path('sports/', views.sports, name='sports-news'),
]  