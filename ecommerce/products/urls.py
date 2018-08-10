from django.conf.urls import url
from products.views import ProductsList, product_list_view

urlpatterns =[
    url(r'^ls/$', ProductsList.as_view()),
    url(r'^ls-basic/$', product_list_view),
]