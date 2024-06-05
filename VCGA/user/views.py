from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView

from .forms import (
    StaffSignupForm,
    StudentSignupForm
    )

# Create your views here.


class ManagementLoginView(LoginView):
    template_name = 'dashboard/user/login.html'

    def get_success_url(self) -> str:
        print(self.request.user.is_student)
        if (self.request.user.is_superuser):
            url = '/admin'
        elif (self.request.user.is_staff):
            url = '/university/'
        elif (self.request.user.is_student):
            url = '/student/'
        else:
            url = '/'
        return url


def student_register(request, *args, **kwargs):
    if request.method == "POST":
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-home")

    else:
        form = StudentSignupForm()
    context = {
        "form": form,
        "title": "Student Register"
    }
    return render(request, "dashboard/student/student-register.html", context)


def faculty_register(request, *args, **kwargs):
    if request.method == "POST":
        form = StaffSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("faculty-home")

    else:
        form = StaffSignupForm()
    context = {
        "form": form,
        "title": "Faculty Register"
    }
    return render(request, "dashboard/faculty/faculty-register.html", context)
