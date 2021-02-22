from django.urls import include, path
from .views import ProductList

urlpatterns = [
    path('', ProductList.as_view(), name='product')
]
