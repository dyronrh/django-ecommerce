from django.conf.urls import url
from products.views import ProductsList, product_list_view, ProductsDetailView, product_detail_view

urlpatterns =[
    url(r'^ls/$', ProductsList.as_view()),
    url(r'^ls-basic/$', product_list_view),
    url(r'^detail/(?P<pk>\d+)/$', ProductsDetailView.as_view()),
    url(r'^detail-basic/(?P<pk>\d+)/$', product_detail_view),
]