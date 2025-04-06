from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('sdata', views.home, name='home'),
    path('sdata/families', views.families, name='families'),
    path('sdata/events', views.events, name='events'),
    path('sdata/institutions', views.institutions, name='institutions'),
]