from django.shortcuts import render

from user.decorators import staff_required
# Create your views here.


@staff_required
def home(request, *args, **kwargs):
    context = {
        'title': 'Faculty Dashboard',
        'name': 'Faculty',
    }
    return render(
        request=request,
        template_name='dashboard/faculty/faculty_dashboard.html',
        context=context
        )
