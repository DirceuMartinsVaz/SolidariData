from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('sdata', views.home, name='home'),
    # Families paths:
    path('sdata/family', views.family_list, name='family_list'),  # List all families
    path('sdata/family/<int:pk>/', views.family_detail, name='family_detail'),  # View details of a specific family
    path('sdata/family/create/', views.family_create, name='family_create'),  # Create a new family
    path('sdata/family/<int:pk>/update/', views.family_update, name='family_update'),  # Update a specific family
    path('sdata/family/<int:pk>/delete/', views.family_delete, name='family_delete'),  # Delete a specific family
    #
    #path('sdata/families', views.families, name='families'),
    path('sdata/events', views.events, name='events'),
    path('sdata/institutions', views.institutions, name='institutions'),
]