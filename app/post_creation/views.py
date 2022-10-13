from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Model
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from core.models import News
from post_creation.forms import PostCreationForm
from post_creation.services import send_email_to_staff_members


class NewsCreateView(UserPassesTestMixin, CreateView):
    """View for the news creation form"""

    model: Model = News
    form_class = PostCreationForm
    template_name = "news/news-creation.html"
    success_url = reverse_lazy("news-list")

    def test_func(self) -> bool:
        """Tests if user is staff"""
        return self.request.user.is_staff

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Assign the post author before saving the data"""
        form.instance.author = self.request.user
        send_email_to_staff_members(self.request.user)
        return super().form_valid(form)
