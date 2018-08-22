from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from products.models import Product
from django.http import Http404
# Create your views here.

class ProductsList(ListView):
    queryset = Product.objects.all()
    template_name = 'ecommerce/product_list_view.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ProductsList, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    template_name = 'ecommerce/product_list_view.html'
    return render(request, "products/list.html", context)


class ProductsDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'ecommerce/product_detail_view.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ProductsDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def product_detail_view(request, pk=None,  *args, **kwargs):
    print(args)
    print(kwargs)
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    qs = Product.objects.filter(pk = pk)
    print(qs)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product does't exist")

    context = {
        'object': instance
    }
    template_name = 'ecommerce/product_detail_view.html'
    return render(request, "products/detail.html", context)
