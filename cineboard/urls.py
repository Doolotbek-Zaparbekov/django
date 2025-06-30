from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/add/', MovieCreateView.as_view(), name='movie_add'),
    path('movie/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]