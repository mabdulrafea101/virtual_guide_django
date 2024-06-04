from django.urls import path

from .views import home
urlpatterns = [
    path('', home, name="faculty-home"),
    path('event/create/', home, name='event-create'),
    path('event/detail/<int:pk>/', home, name='event-detail'),
    path('event/update/<int:pk>/', home, name='event-update'),
]
