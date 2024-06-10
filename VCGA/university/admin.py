from django.contrib import admin

from .models import Event, EventCategory, Comment
# Register your models here.
admin.site.register(Event)
admin.site.register(EventCategory)
# admin.site.register(Image)
admin.site.register(Comment)
