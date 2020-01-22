from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
def home(request):
   url = 'https://api.currentsapi.services/v1/search?keywords=Amazon&language=en&apiKey=dBdy9d2EsMbrOnT6nDA6ygdFEIy-qB98zMBzpfF77Sqy8BS2'
   
   response = requests.get(url).json()
   # print (response.text)
   context = {
      'responses': response['news']
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
