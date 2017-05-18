
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib import admin

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Tags(models.Model):
   post = models.ForeignKey(Post, related_name='tags')
   tags = models.TextField()

class TagsInline(admin.StackedInline):
    model = Tags

class TagsAdmin(admin.ModelAdmin):
    inlines = [
        TagsInline,
    ]