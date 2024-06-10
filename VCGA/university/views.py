from django.shortcuts import render
from django.views.generic import CreateView

from .forms import EventForm
from .models import Event, EventCategory
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


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "dashboard/faculty/events/create.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
