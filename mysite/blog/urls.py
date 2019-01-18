from django.conf.urls import urls,include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [url('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25]),
												template_name="blog/blog.html")]