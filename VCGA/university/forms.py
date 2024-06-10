from django import forms
from .models import EventCategory, Event
from django.utils.translation import gettext_lazy as _


class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ["name", "description", "image"]
        labels = {
            "name": _("Category Name"),
            "description": _("Describe category purpose"),
            "image": _("Upload Image"),
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "content", "category", "image")
        labels = {
            "title": _("Event Name"),
            "content": _("Details"),
            "category": _("Select Category"),
            "image": _("Upload Image"),
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                },       
            ),

        }
