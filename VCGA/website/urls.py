from django.urls import path

from .views import (
    home, about, contact_us,
    teacher_view, pricing, courses,
    campus_maps
    )
urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about-us"),
    path('contact-us/', contact_us, name="contact-us"),
    path('our-teachers/', teacher_view, name="teacher-view"),
    path('our-fee/', pricing, name="our-fee"),
    path('courses/', courses, name="courses"),
    path('campus-map/', campus_maps, name="campus-map"),
]
