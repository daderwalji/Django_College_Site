from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'clg-home'),
    path('about/', views.about, name='clg-about'),
    path('admission/', views.admission, name='clg-admission'),
    path('contact/', views.contact, name='clg-contact'),
]