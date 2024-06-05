from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
# from phonenumber_field.formfields import PhoneNumberField

# from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ["username", "password"]:
            self.fields[fieldname].widget.attrs = {"class": "form-control",
                                                   "placeholder": fieldname}


class AdminSignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Your valid email address",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = True
        user.save()
        return user


class StudentSignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Your valid email address",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_student = True
        user.save()
        return user


class StaffSignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="Optional",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Your valid email address",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self):
        user = super().save(commit=False)
        user.is_superuser = False
        user.is_staff = True
        user.save()
        return user
