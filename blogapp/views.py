from django.shortcuts import render
from django.conf.urls import url
from django.conf.urls import include

# Create your views here.
def post_list(request):
    return render(request, 'blogapp/post_list.html', {})