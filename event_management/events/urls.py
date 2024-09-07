# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('events/', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('category/<int:pk>/', views.events_by_category, name='events_by_category'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:pk>/register/', views.register_event, name='register_event'),
]
