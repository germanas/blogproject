from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blogapp.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='blogapp/robots.txt')),

]
