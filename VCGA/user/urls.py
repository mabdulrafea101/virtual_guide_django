from django.urls import path, reverse_lazy

from django.contrib.auth.views import LogoutView

from .forms import MyLoginForm
from .views import ManagementLoginView, student_register, faculty_register

urlpatterns = [
    path("login/",
         ManagementLoginView.as_view(
            
            authentication_form=MyLoginForm,
            ), name="login", ),
    path("logout/", LogoutView.as_view(
        template_name="user/logout.html",
        next_page=reverse_lazy("home")
    ), name="logout"),
    path('student/register/', student_register, name='student-register'),
    path('faculty/register/', faculty_register, name='faculty-register'),
]
