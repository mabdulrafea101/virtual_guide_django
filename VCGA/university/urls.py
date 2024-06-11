from django.urls import path

from .views import home, EventCreateView, EventListView
urlpatterns = [
    path('', home, name="faculty-home"),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/list/', EventListView.as_view(), name='event-list'),
    path('event/detail/<int:pk>/', home, name='event-detail'),
    path('event/update/<int:pk>/', home, name='event-update'),
]
