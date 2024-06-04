from django.shortcuts import render

from .forms import MyLoginForm, FacultySignupForm, StudentSignupForm

# Create your views here.


def login(request, *args, **kwargs):
    context = {
        'title': 'Login',
    }

    return render(request=request,
                  template_name='dashboard/user/login.html',
                  context=context,
                  )


def student_register(request, *args, **kwargs):
    context = {
        'title': 'Student Register',
    }
    return render(request=request,
                  template_name='dashboard/student/student-register.html',
                  context=context,
                  )


def faculty_register(request, *args, **kwargs):
    context = {
        'title': 'Faculty Register',
    }
    return render(request=request,
                  template_name='dashboard/faculty/faculty-register.html',
                  context=context,
                  )
