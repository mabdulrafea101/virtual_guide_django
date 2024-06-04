from django.urls import path

from .views import student_home, student_map
urlpatterns = [
    path('', student_home, name="student-home"),
    path('maps/',
         student_map,
         name="student-map"),
]
