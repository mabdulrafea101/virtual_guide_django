from django.urls import path

from .views import home, EventCreateView
urlpatterns = [
    path('', home, name="faculty-home"),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/list/', home, name='event-list'),
    path('event/detail/<int:pk>/', home, name='event-detail'),
    path('event/update/<int:pk>/', home, name='event-update'),
]
