from django.urls import path

from news_details.views import NewsDetailView

urlpatterns = [path("<int:pk>/", NewsDetailView.as_view(), name="news-detail")]
