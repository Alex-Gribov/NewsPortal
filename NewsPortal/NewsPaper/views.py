# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import News
from .templatetags.filters import censor

def news_list(request):
    articles = News.objects.all().order_by('-published_date')  # Получаем все статьи
    for article in articles:
        article.title = censor(article.title)  # Применяем фильтр к заголовкам
        article.content = censor(article.content)  # Применяем фильтр к содержимому
    return render(request, 'NewsPaper/news_list.html', {'articles': articles})

def news_detail(request, news_id):
    article = get_object_or_404(News, id=news_id)
    return render(request, 'NewsPaper/news_detail.html', {'article': article})

def home(request):
    return render(request, 'NewsPaper/default.html')