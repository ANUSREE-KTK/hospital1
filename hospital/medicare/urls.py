from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.department,name='department'),
    path('contact/', views.booking,name='booking'),
    path('about/', views.doctors,name='doctors'),
    
]