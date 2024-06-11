from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

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
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'dashboard/faculty/events/list.html'


class MyEventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'dashboard/faculty/events/my-list.html'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'dashboard/faculty/events/detail.html'


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "dashboard/faculty/events/update.html"
    success_url = reverse_lazy('event-list')


class EventDeleteView(DeleteView):
    model = Event
    template_name = "dashboard/faculty/events/delete.html"
    success_url = reverse_lazy('event-list')
