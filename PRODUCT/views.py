from django.views.generic import ListView
from PRODUCT.models import Product


class ProductCategoryListView(ListView):
    template_name = 'product/product_search_view.html'

    def get_queryset(self):
        result = self.kwargs.get('category')
        return Product.objects.filter(category__category__iexact=result)
