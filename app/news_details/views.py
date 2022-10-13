from django.views.generic import DetailView

from core.models import News


class NewsDetailView(DetailView):
    """Detailed view for news objects"""

    model = News
    context_object_name = "news"
    template_name = "news/news-detail.html"
