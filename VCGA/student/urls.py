from django.urls import path

from .views import (
    EventListViewByCategory,
    StudentEventDetail,
    event_participate,
    event_un_participate,
    events_by_category,
    student_home,
    student_map,
    EventListView,
    EventCagetoryListView,
    ParticipatedEventListView,
    DocumentList
    )

urlpatterns = [
    path('', student_home, name="student-home"),
    path('documents/', DocumentList.as_view(), name="student_document_list"),
    path('maps/',
         student_map,
         name="student-map"),
    path(
        'events/',
        EventListView.as_view(),
        name="student-events-list"
    ),
    path(
        'event/<int:pk>',
        StudentEventDetail.as_view(),
        name="student-event-detail"
    ),
    path(
        'events/category/',
        EventCagetoryListView.as_view(),
        name="student-events-category-list"
    ),
    path(
        'events/category/<int:pk>',
        events_by_category,
        name="events-by-category"
    ),
    path(
        'categories/<int:category_id>/events/',
        EventListViewByCategory.as_view(),
        name='event_list_by_category'),
    path(
        'events/participated/list/',
        ParticipatedEventListView.as_view(),
        name="student-events-participated-list"
    ),
    path(
        'events/participate/<int:pk>/',
        event_participate,
        name="student-events-participate"
    ),
    path(
        'events/un-participate/<int:pk>/',
        event_un_participate,
        name="student-events-un-participate"
    ),
]
