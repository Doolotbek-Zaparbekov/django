from django.urls import path
from . import views

urlpatterns = [
    path('news_book/', views.BookListView.as_view(), name='news_book'),
    path('news_book/<int:id>/', views.BookDetailView.as_view(), name='news_book_detail'),
    path('books/', views.StaticBookView.as_view(), name='books'),
    path('news_book/<int:book_id>/book_id_audio_recording/', views.AudioBookView.as_view(), name='audio_recording'),
    path('', views.BookSearchListView.as_view(), name='book_list'),
]
