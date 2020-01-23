from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings

# Create your views here.
def home(request):
   # This API endpoint will get the latest news from Current news API
   currentapi_base_url ='https://api.currentsapi.services/v1/latest-news?&apiKey={}'
   newsapi_base_url= 'https://newsapi.org/v2/top-headlines?language=en&apiKey={}'
   
   ###### FETCH NEWS IN FROM THE NEWSAPI.ORG #######
   newsapi_url=newsapi_base_url.format(settings.NEWS_API_KEY)
   news = requests.get(newsapi_url).json()   
   
   #### FETCH NEWS FROM THE CURRENT API #####
   currentapi_url=currentapi_base_url.format(settings.CURRENT_API_KEY)
   response = requests.get(currentapi_url).json()
   
       
   ####### WHAT GETS DISPLAYED IN THE VIEW #########   
   context = {
      'responses': news['articles']
   }     
    
   return render(request,'news/home.html', context)
  
def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         messages.success(request, f'Your account has been created! You are now able to log in')
         return redirect('login')
   else:
      form = UserRegisterForm()
   return render(request, 'users/register.html', {'form': form})

@login_required(login_url='/login/')
def profile(request):
   user = request.user
   return render(request, 'users/profile.html')
