from django.urls import path
from . import views


urlpatterns = [
  path('news_book/', views.book_list_view, name='news_book'),
  path('news_book/<int:id>/', views.book_detail_view, name='news_book_detail'),
  path('books/', views.books, name='books'),
  path('news_book/<int:book_id>/book_id_audio_recording/', views.your_view_function, name='audio_recording/')
]
