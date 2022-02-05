from django.views.generic import TemplateView
from .models import SliderImages
from PRODUCT.models import Product


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['slider_images'] = SliderImages.objects.all()
        context['latest_books'] = Product.objects.all().order_by('-id')[:5]
        return context


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactView(TemplateView):
    template_name = 'home/contact_us.html'
