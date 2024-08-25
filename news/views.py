from django.shortcuts import render
from .models import News


# Create your views here.

def news_view(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})
