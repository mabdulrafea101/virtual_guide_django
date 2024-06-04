from django.shortcuts import render

# Create your views here.


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


def student_map(request, *args, **kwargs):
    context = {
        'title': 'Map - Student'
    }
    return render(request=request,
                  template_name='dashboard/student/maps.html',
                  context=context
                  )
