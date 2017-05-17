from django.conf.urls import url, include
from . import views
from django.http import HttpResponse


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),


]