from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _


class AuthenticationForm(auth_forms.AuthenticationForm):
    """Form for logging in"""

    username_field_attributes = {
        "autofocus": True,
        "class": "form-control",
    }
    password_field_attributes = {
        "autocomplete": "current-password",
        "class": "form-control",
    }

    username = auth_forms.UsernameField(
        widget=forms.TextInput(attrs=username_field_attributes)
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs=password_field_attributes),
    )
