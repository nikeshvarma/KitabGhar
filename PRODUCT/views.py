from django.views.generic import ListView, DetailView
from PRODUCT.models import Product


class ProductCategoryListView(ListView):
    template_name = 'product/product_search_view.html'

    def get_queryset(self):
        result = self.kwargs.get('category')
        return Product.objects.filter(category__category__iexact=result)


class ProductDetailView(DetailView):
    template_name = 'product/product_details.html'

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs.get('id'))
