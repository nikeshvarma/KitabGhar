from django.urls import path
from .views import ProductCategoryListView, ProductDetailView

urlpatterns = [
    path('category/<str:category>/', ProductCategoryListView.as_view(), name='product_category_view'),
    path('details/<str:id>/', ProductDetailView.as_view(), name='product_detail_view')
]
