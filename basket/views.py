from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from .forms import BasketForm

def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm()
    return render(request, 'basket_create.html', {'form': form})

def basket_list_view(request):
    baskets = Basket.objects.all()
    return render(request, 'basket_list.html', {'baskets': baskets})

def update_basket_view(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = BasketForm(instance=basket)
    return render(request, 'basket_update.html', {'form': form})

def delete_basket_view(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        basket.delete()
        return redirect('basket_list')
    return render(request, 'basket_delete.html', {'basket': basket})
