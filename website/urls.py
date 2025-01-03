from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('counselor/', views.counselor, name = 'counselor'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('services/', views.services, name = 'services'),

]