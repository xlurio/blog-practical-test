from django.utils.decorators import method_decorator
from django.views.decorators.http import last_modified
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django.views.generic import ListView

from core.models import News
from news_listing.services import get_lastest_post_date


@method_decorator(vary_on_cookie, name="get")
@method_decorator(vary_on_headers("Last-Modified"), name="get")
@method_decorator(last_modified(get_lastest_post_date), name="get")
class NewsListView(ListView):
    """View for listing all stored news"""

    queryset = News.objects.order_by("-publication_date")
    context_object_name = "news_set"
    paginate_by = 10
    template_name = "news/news-list.html"
