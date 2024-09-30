from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News


# Create your views here.

def news_view(request):
    news = News.objects.all().order_by('created_at')
    paginator = Paginator(news, 10) # 10 news items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the page of news

    return render(request, 'news.html', {'page_obj': page_obj})
