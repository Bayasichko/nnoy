from django.shortcuts import render
from .models import *

def main_page(request):
  contacts = Contact.objects.all()[0]
  articles = Article.objects.all().filter(is_on_feed=True)
  main_page_info = MainPage.objects.all()[0]

  context = {
    'contacts': contacts,
    'articles': articles,
    'main_page_info': main_page_info,
  }

  return render(request, 'index.html', context)

def news_page(request):
  contacts = Contact.objects.all()[0]
  articles = Article.objects.all()
  category = Category.objects.all()
  main_page_info = MainPage.objects.all()[0]

  context = {
    'contacts': contacts,
    'category': category,
    'articles': articles,
    'main_page_info': main_page_info,
  }

  return render(request, 'news.html', context)