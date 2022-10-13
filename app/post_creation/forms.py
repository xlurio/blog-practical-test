from django import forms

from core.models import Category, News


class PostCreationForm(forms.ModelForm):
    """Form for making posts"""

    title_field_attributes = {"class": "form-control"}
    category_field_attributes = {"class": "form-select"}
    content_field_attributes = {
        "rows": 255,
        "class": "form-control not-resizable",
        "placeholder": "Tell me the news...",
    }

    title = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs=title_field_attributes)
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs=category_field_attributes,
        ),
        required=False,
    )
    content = forms.CharField(widget=forms.Textarea(attrs=content_field_attributes))

    class Meta:
        """Form meta data"""

        model = News
        fields = ["title", "category", "content"]
