from django.shortcuts import render

from user.decorators import student_required

# Create your views here.


@student_required
def student_home(request, *args, **kwargs):
    context = {
        'title': 'Student Dashboard',
        'name': 'student'
    }
    return render(
        request=request,
        template_name='dashboard/student/student_dashboard.html',
        context=context
        )


@student_required
def student_map(request, *args, **kwargs):
    context = {
        'title': 'Map - Student'
    }
    return render(request=request,
                  template_name='dashboard/student/maps.html',
                  context=context
                  )
