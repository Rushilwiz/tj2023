from django.db import models


# Create your models here.
class Story(models.Model):
    header = models.CharField(max_length=50)
    img_name = models.CharField(max_length=50, default=None, null=True)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header


class Bar(models.Model):
    name = models.CharField(max_length=70)
    money_raised = models.FloatField()
