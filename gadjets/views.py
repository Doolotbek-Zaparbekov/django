from django.views.generic import ListView
from .models import Product, Tag

class ProductListView(ListView):
    model = Product
    template_name = 'gadjets/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        tag_name = self.request.GET.get('tag')
        return Product.objects.filter(tags__name=tag_name) if tag_name else Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
