from .models import Basket
from .forms import BasketForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BasketCreateView(CreateView):
    model = Basket
    form_class = BasketForm
    template_name = 'basket_create.html'
    success_url = reverse_lazy('basket_list')

class BasketListView(ListView):
    model = Basket
    template_name = 'basket_list.html'
    context_object_name = 'baskets'

class BasketUpdateView(UpdateView):
    model = Basket
    form_class = BasketForm
    template_name = 'basket_update.html'
    success_url = reverse_lazy('basket_list')

class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'basket_delete.html'
    success_url = reverse_lazy('basket_list')
