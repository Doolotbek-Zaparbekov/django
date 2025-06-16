from django.urls import path
from . import views

urlpatterns = [
    path('basket/create/', views.create_basket_view, name='create_basket'),
    path('', views.basket_list_view, name='basket_list'),
    path('basket/update/<int:pk>/', views.update_basket_view, name='update_basket'),
    path('basket/delete/<int:pk>/', views.delete_basket_view, name='delete_basket'),
]
