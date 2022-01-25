from django.views.generic import TemplateView
from .models import SliderImages


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['slider_images'] = SliderImages.objects.all()
        return context
