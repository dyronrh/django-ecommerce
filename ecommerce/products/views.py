from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product
# Create your views here.

class ProductsList(ListView):
    queryset = Product.objects.all()
    template_name = 'ecommerce/product_list_view.html'


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "ecommerce/product_list_view.html", context)
