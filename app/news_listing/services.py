from django.http import HttpRequest

from core.models import News


def get_lastest_post_date(request: HttpRequest):
    return News.objects.latest("publication_date").publication_date
