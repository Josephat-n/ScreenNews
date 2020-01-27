from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.welcome, name ='screen-welcome'),
   path('home/', views.home, name ='screen-home'),
   path('profile/', views.profile, name='user-profile'),
   path('sports/', views.sports, name='sports-news'),
   path('business/', views.business, name='business-news'),
   path('politics/', views.business, name='politics-news'),
   # path('article/<str:url>', views.article, name='news-article'),
   path('article/', views.article, name='news-article'),
   path('search/', views.search, name='article-search'),
]  