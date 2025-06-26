from django.urls import path
from .views import BasketCreateView, BasketListView, BasketUpdateView, BasketDeleteView

urlpatterns = [
    path('basket/create/', BasketCreateView.as_view(), name='create_basket'),
    path('', BasketListView.as_view(), name='basket_list'),
    path('basket/update/<int:pk>/', BasketUpdateView.as_view(), name='update_basket'),
    path('basket/delete/<int:pk>/', BasketDeleteView.as_view(), name='delete_basket'),
]