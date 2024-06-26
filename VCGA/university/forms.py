from django import forms
from .models import Document, EventCategory, Event
from django.utils.translation import gettext_lazy as _


class EventCategoryForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    
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
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Event
        fields = ("title",
                  "content", 
                  "category", 
                  "image", 
                  "start_at", 
                  "ends_at")
        labels = {
            "title": _("Event Name"),
            "content": _("Details"),
            "category": _("Select Category"),
            "image": _("Upload Image"),
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "aria-label": "event-name",
                    "placeholder": "Event Name",
                    "aria-describedby": "basic-addon1",
                }
            ),
            "content": forms.Textarea(
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
            "start_at": forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            ),
            "ends_at": forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            ),

        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'description', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }