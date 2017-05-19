import re
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.CharField(default='change this',max_length=200)
    text = RichTextField()
    tags = models.CharField(default='default_tag',max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def get_tag_list(self):
        return re.split(",", self.tags)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

