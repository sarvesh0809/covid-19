from django.urls import path
from rem import views
urlpatterns = [
    path('',views.index, name='home'),
    path('home',views.home),
    path('city',views.city),
    path('totals',views.totals)
]