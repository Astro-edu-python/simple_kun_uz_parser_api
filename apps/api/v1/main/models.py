from django.db import models


class KunUzNews(models.Model):
    link = models.URLField('Link', max_length=1000)
    preview_link = models.URLField(
        'Preview link', max_length=1000, null=True, blank=True
    )
    title = models.TextField('Title', unique=True)

    def __str__(self):
        return self.title
