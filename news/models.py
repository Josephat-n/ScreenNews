from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   name = models.CharField(max_length =30)
   email = models.CharField(max_length =30)
   
class Article(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE, default = 1)
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=300)
   url = models.CharField(max_length=1000)
   author = models.CharField(max_length=50)
   date = models.CharField(max_length=40)
   
   def __str__(self):
      return self.title

   def save_project(self):
      """
      Save a new article to the database    
      """
      self.save()
      
   @classmethod
   def get_all(cls):
      """
      This function allows for the fetching of all saved news articles from the database
      """
      articles = Article.objects.all()
      return articles   