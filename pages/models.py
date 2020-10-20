from django.db import models


# Create your models here.
class Story(models.Model):
    header = models.CharField(max_length=30)
    img_name = models.CharField(max_length=50, default=None, null=True)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now=True)