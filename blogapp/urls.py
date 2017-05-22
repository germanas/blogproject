from django.conf.urls import url, include
from . import views
from blogapp.views import post_list

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^/page/(?P<page>\d+)/$', post_list),

]