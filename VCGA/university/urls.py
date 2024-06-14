from django.urls import path

from .views import (
    DocumentCreateView,
    DocumentListView,
    home,
    EventCreateView,
    EventListView,
    EventUpdateView,
    EventDetailView,
    MyEventListView,
    EventDeleteView
    )
urlpatterns = [
    path('', home, name="faculty-home"),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/list/', EventListView.as_view(), name='event-list'),
    path('event/my/list/', MyEventListView.as_view(), name='my-event-list'),
    path('event/detail/<int:pk>/', 
         EventDetailView.as_view(), 
         name='event-detail'),
    path('event/update/<int:pk>/', 
         EventUpdateView.as_view(), 
         name='event-update'),
    path('event/delete/<int:pk>/', 
         EventDeleteView.as_view(), 
         name='event-delete'),

    path('documents/', DocumentListView.as_view(), name='document_list'),
    path('documents/add/', DocumentCreateView.as_view(), name='document_add'),
]
