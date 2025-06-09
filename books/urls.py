from django.urls import path
from . import views

urlpatterns = [
  path('news_book/', views.book_list_view, name='news_book'),
  path('news_book/<int:id>/', views.book_detail_view, name='news_book_detail'),
  path('books/', views.books, name='books'),
]