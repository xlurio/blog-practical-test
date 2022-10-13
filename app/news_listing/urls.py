from django.urls import path

from news_listing.views import NewsListView

urlpatterns = [path("", NewsListView.as_view(), name="news-list")]
