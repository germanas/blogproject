
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
  sidebar = Post.objects.all()
  paginator = Paginator(posts, 2)  # Show 25 contacts per page
  page = request.GET.get('page')
  try:
      posts = paginator.page(page)
  except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      posts = paginator.page(1)
  except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      posts = paginator.page(paginator.num_pages)

  return render(request, 'blogapp/post_list.html',  {'posts': posts, 'sidebar':sidebar})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blogapp/post_detail.html', {'post': post})