from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('contact-us/', views.ContactView.as_view(), name='contact_us_view')
]
