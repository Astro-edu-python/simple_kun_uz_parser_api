from celery.app import shared_task
from django.conf import settings

from apps.api.v1.main.models import KunUzNews
from services.kun_uz_parser.parser import parse_news


@shared_task
def parse_news_task_beat():
    news = parse_news(settings.KUN_UZ_MAIN_URL)
    db_news_links = list(
        KunUzNews.objects.values_list('link', flat=True).all()
    )
    KunUzNews.objects.bulk_create([
        KunUzNews(
            title=post.title.strip(),
            link=post.link,
            preview_link=post.preview_link
        )
        for post in news if post.link not in db_news_links
    ])
