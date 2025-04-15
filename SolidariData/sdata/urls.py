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
    # Event URLs
    path('sdata/events/', views.event_list, name='event_list'),
    path('sdata/events/<int:pk>/', views.event_detail, name='event_detail'),
    path('sdata/events/create/', views.event_create, name='event_create'),
    path('sdata/events/<int:pk>/update/', views.event_update, name='event_update'),
    path('sdata/events/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('sdata/events/<int:event_pk>/toggle-institution/<int:institution_pk>/', views.toggle_institution_signup, name='toggle_institution_signup'),
    path('sdata/events/<int:event_pk>/families/', views.event_family_list, name='event_family_list'),
    path('sdata/events/<int:event_pk>/manage-families/', views.manage_event_families, name='manage_event_families'),
    path('sdata/events/<int:event_pk>/toggle-family-served/<int:family_pk>/', views.toggle_family_served, name='toggle_family_served'),
    path('events/<int:event_pk>/manage-served-status/', views.manage_served_status, name='manage_served_status'),

    # Institution URLs
    path('sdata/institutions/', views.institution_list, name='institution_list'),
    path('sdata/institutions/<int:pk>/', views.institution_detail, name='institution_detail'),
    path('sdata/institutions/create/', views.institution_create, name='institution_create'),
    path('sdata/institutions/<int:pk>/update/', views.institution_update, name='institution_update'),
    path('sdata/institutions/<int:pk>/delete/', views.institution_delete, name='institution_delete'),

    # Institution Representative URLs
    path('sdata/institutions/<int:institution_pk>/representatives/', views.institution_representative_list, name='institution_representative_list'),
    path('sdata/institutions/<int:institution_pk>/representatives/create/', views.institution_representative_create, name='institution_representative_create'),
    path('sdata/institutions/<int:institution_pk>/representatives/<int:pk>/update/', views.institution_representative_update, name='institution_representative_update'),
    path('sdata/institutions/<int:institution_pk>/representatives/<int:pk>/delete/', views.institution_representative_delete, name='institution_representative_delete'),

    # InstitutionEvent URLs
    path('sdata/institution-events/', views.institution_event_list, name='institution_event_list'),
    path('sdata/institution-events/create/', views.institution_event_create, name='institution_event_create'),
    path('sdata/institution-events/<int:pk>/delete/', views.institution_event_delete, name='institution_event_delete'),

    # FamilyEvent URLs
    path('sdata/family-events/', views.family_event_list, name='family_event_list'),
    path('sdata/family-events/create/', views.family_event_create, name='family_event_create'),
    path('sdata/family-events/<int:pk>/delete/', views.family_event_delete, name='family_event_delete'),

    # FamilyEventInstitution URLs
    path('sdata/family-event-institutions/', views.family_event_institution_list, name='family_event_institution_list'),
    path('sdata/family-event-institutions/create/', views.family_event_institution_create, name='family_event_institution_create'),
    path('sdata/family-event-institutions/<int:pk>/delete/', views.family_event_institution_delete, name='family_event_institution_delete'),
]