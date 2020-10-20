from django.db import models
from django.conf import settings
from notion.client import NotionClient

client = NotionClient(token_v2=settings.NOTION_COOKIE)


# Create your models here.
class NotionPage(models.Model):
    url = models.URLField(max_length=300)
    page = None

    def __init__(self, *args, **kwargs):
        super(NotionPage, self).__init__(*args, **kwargs)
        if self.url:
            self.page = client.get_block(self.url)

    def __str__(self):
        return str(self.page and self.page.title)
