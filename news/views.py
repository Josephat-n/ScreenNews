from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from .models import Article

# Create your views here.
def welcome(request):   
   
   return render(request,'news/welcome.html')

def home(request):
   all_news = []
   # This API endpoint will get the latest news from Current news API
   currentapi_base_url ='https://api.currentsapi.services/v1/latest-news?&apiKey={}'
   newsapi_base_url= 'https://newsapi.org/v2/top-headlines?language=en&apiKey={}'
   
   ##### FETCH NEWS IN FROM THE NEWSAPI.ORG #######
   newsapi_url=newsapi_base_url.format(settings.NEWS_API_KEY)
   # news = requests.get(newsapi_url).json()
   newsList = requests.get(newsapi_url).json()['articles']
   
   for item in newsList:
      newsitem = {}
      newsitem['title'] = item['title']
      newsitem['description'] = item['description']
      newsitem['url'] = item['url']
      newsitem['author'] = item['author']
      newsitem['image'] = item['urlToImage'] 
      newsitem['date'] = item['publishedAt']      
   all_news.append(newsitem)    
       
   #### FETCH NEWS FROM THE CURRENT API #####
   # currentapi_url=currentapi_base_url.format(settings.CURRENT_API_KEY)
   # resList = requests.get(currentapi_url).json()['news']
   
   # for item in resList:
   #    newsArticle = {}
   #    newsArticle['title'] = item['title']
   #    newsArticle['description'] = item['description']
   #    newsArticle['url'] = item['url']
   #    newsArticle['author'] = item['author']
   #    newsArticle['image'] = item['image'] 
   #    newsArticle['date'] = item['published']      
   # all_news.append(newsArticle) 
            
   # ####### WHAT GETS DISPLAYED IN THE VIEW #########   
   context = {
      # 'responses': all_news['item']
      'responses': all_news
   }     
   
   return render(request,'news/home.html', context)

def sports(request):
   sports_news= []
   #### FETCH SPORTS NEWS FROM THE CURRENT API #####
   currentapi_base_url = 'https://api.currentsapi.services/v1/search?category={}&apiKey={}'
   sports_url = currentapi_base_url.format(sports,settings.CURRENT_API_KEY)
   sportsList = requests.get(sports_url).json()['news']   
   
   for item in sportsList:
      newsitem = {}
      newsitem['title'] = item['title']
      newsitem['description'] = item['description']
      newsitem['url'] = item['url']
      newsitem['author'] = item['author']
      newsitem['image'] = item['image'] 
      newsitem['date'] = item['published']      
      sports_news.append(newsitem) 
   
   context = {
      'responses': sports_news
   }   
   return render(request,'news/sports.html', context)
   
def business(request):
   sports_news= []
   #### FETCH SPORTS NEWS FROM THE CURRENT API #####
   currentapi_base_url = 'https://api.currentsapi.services/v1/search?category={}&apiKey={}'
   sports_url = currentapi_base_url.format(business,settings.CURRENT_API_KEY)
   sportsList = requests.get(sports_url).json()['news']   

   for item in sportsList:
      newsitem = {}
      newsitem['title'] = item['title']
      newsitem['description'] = item['description']
      newsitem['url'] = item['url']
      newsitem['author'] = item['author']
      newsitem['image'] = item['image'] 
      newsitem['date'] = item['published']      
      sports_news.append(newsitem) 

   context = {
      'responses': sports_news
   }   
   return render(request,'news/business.html', context)

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

def article(request):
   """
   This page allows for the viewing of a single page of news within an iframe block
   """   
   # context =  {'url':url}
   # return render (request, 'news/article.html',context)
   return render (request, 'news/article.html')

def search(request):
   """
   This function allows a user to search a news article
   """
   if 'article' in request.GET and request.GET["article"]:
      search_output= []
      search_term = request.GET.get("article")
      search_base_url = 'https://api.currentsapi.services/v1/search?keywords={}&language=en&apiKey={}'
      search_url = search_base_url.format(search_term,settings.CURRENT_API_KEY)
      searchList = requests.get(search_url).json()['news'] 
      
      for item in searchList:
         newsitem = {}
         newsitem['title'] = item['title']
         newsitem['description'] = item['description']
         newsitem['url'] = item['url']
         newsitem['author'] = item['author']
         newsitem['image'] = item['image'] 
         newsitem['date'] = item['published']      
         search_output.append(newsitem) 

      context = {'responses': search_output}    
      return render (request, 'news/search.html', context)
   
   else:
      message = "You haven't searched for any term"
      return render(request, 'news/search.html',{"message":message})