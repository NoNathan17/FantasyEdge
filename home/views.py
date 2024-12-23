from django.shortcuts import render
from news.models import News

# Create your views here.
def home_view(request):
    news_items = News.objects.all()
    return render(request, 'home.html', {'news_items': news_items})

def coming_soon_view(request):
    return render(request, 'coming_soon.html')