from django.contrib import admin

from .models import Event, EventCategory, Comment, Document
# Register your models here.
admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Document)
admin.site.register(Comment)
