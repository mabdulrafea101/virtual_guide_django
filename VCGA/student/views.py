from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView,)
from django.db.models import Count

from .forms import CommentForm

from .models import ParticipatedEvent
from website.models import UniversityLocation
from university.models import Comment, Document, Event, EventCategory
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
    maps = UniversityLocation.objects.all()
    context = {
        'title': 'Map - Student',
        'maps': maps
    }
    return render(request=request,
                  template_name='dashboard/student/maps.html',
                  context=context
                  )


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'dashboard/student/events/all-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        participated_events = ParticipatedEvent.objects.filter(
            participant=user,
            is_participated=True).values_list('event_id', flat=True)
        context['participated_events'] = participated_events
        return context
    

class StudentEventDetail(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'dashboard/student/events/detail.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        event = self.get_object()

        # Get all categories with event counts
        categories = EventCategory.objects.all().annotate(
            event_count=Count('event'))
        half = len(categories) // 2
        categories_col1 = categories[:half]
        categories_col2 = categories[half:]

        # Filter events by the current event's category
        events = Event.objects.filter(category=event.category)
        half = len(events) // 2
        events_col1 = events[:half]
        events_col2 = events[half:]

        # Comments and comment form
        comments = event.comments.all()
        comment_form = CommentForm()

        context["categories_col1"] = categories_col1
        context["categories_col2"] = categories_col2
        context["events_col1"] = events_col1
        context["events_col2"] = events_col2
        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
    
    def post(self, request, *args, **kwargs):
        if 'comment' in request.POST:
            event = self.get_object()
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = event
                comment.author = request.user
                comment.save()
                return redirect(
                    reverse(
                        'student-event-detail',
                        kwargs={'pk': event.pk}))
        return self.get(request, *args, **kwargs)


class ParticipatedEventListView(ListView):
    model = ParticipatedEvent
    context_object_name = 'events'
    template_name = 'dashboard/student/events/participated-list.html'


def events_by_category(request, *args, **kwargs):

    context = {}
    print(kwargs["pk"])
    user = request.user
    participated_events = ParticipatedEvent.objects.filter(
            participant=user,
            is_participated=True).values_list('event_id', flat=True)
    context['participated_events'] = participated_events
    context["events"] = Event.objects.filter(category_id=kwargs["pk"]).all()

    return render(
        request, "dashboard/student/events/event_by_category.html", context)    


def event_participate(request, *args, **kwargs):
    eve = get_object_or_404(Event, id=kwargs['pk'])
    participation, created = ParticipatedEvent.objects.get_or_create(
        participant=request.user,
        event=eve
    )
    participation.is_participated = True
    participation.save()

    return redirect(reverse_lazy("student-events-list"))


def event_un_participate(request, *args, **kwargs):
    eve = get_object_or_404(Event, id=kwargs['pk'])
    participation, created = ParticipatedEvent.objects.get_or_create(
        participant=request.user,
        event=eve
    )
    participation.is_participated = False
    participation.save()

    return redirect(reverse_lazy("student-events-list"))


class EventCagetoryListView(ListView):
    model = EventCategory
    context_object_name = 'categories'
    template_name = 'dashboard/student/events/category-list.html'

    def get_queryset(self):
        return EventCategory.objects.annotate(event_count=Count('event'))
    

class EventListViewByCategory(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'dashboard/student/events/event_by_category.html'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Event.objects.filter(category_id=category_id)


class StudentCommentListView(ListView):
    model = Comment
    context_object_name = 'my-comment'
    template_name = 'dashboard/student/document/document_list.html'


class DocumentList(ListView):
    model = Document
    context_object_name = 'documents'
    template_name = 'dashboard/student/documents/document_list.html'
