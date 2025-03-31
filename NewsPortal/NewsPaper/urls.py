# NewsPaper/urls.py
from django.urls import path
from .views import news_list, news_detail, home

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('news/', news_list, name='news_list'),  # Список новостей
    path('news/<int:news_id>/', news_detail, name='news_detail'),  # Детали новости
]




