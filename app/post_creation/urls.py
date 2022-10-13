from django.urls import path

from post_creation.views import NewsCreateView

urlpatterns = [path("create/", NewsCreateView.as_view(), name="news-create")]
