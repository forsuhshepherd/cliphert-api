from django.conf.urls import url
from .views import ProductsApi, DetailedProductApi, CategoryApi, ProfileApi, DetailedCategoryApi

urlpatterns = [
    url(r'^products/all', ProductsApi.as_view(), name='products'),
    url(r'^product/(?P<pk>\d+)/$', DetailedProductApi.as_view(), name='detailed-product'),
    url(r'^category/(?P<pk>\d+)/$', DetailedCategoryApi.as_view(), name='detailed-category'),
    url(r'^categories/', CategoryApi.as_view(), name='categories'),
    url(r'^profiles/all', ProfileApi.as_view(), name='profiles'),
]
