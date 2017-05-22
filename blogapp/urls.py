from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),

]