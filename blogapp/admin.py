from django.contrib import admin
from blogapp.models import Post, TagsAdmin



admin.site.register(Post, TagsAdmin)

