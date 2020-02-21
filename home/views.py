from django.shortcuts import render
from news.models import Article

def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:3]
    return render(request, 'home/homePage.html', locals())
