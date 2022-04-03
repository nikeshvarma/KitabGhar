from django.urls import path
from .views import ProductCategoryListView

urlpatterns = [
    path('category/<str:category>/', ProductCategoryListView.as_view(), name='product_category_view')
]
