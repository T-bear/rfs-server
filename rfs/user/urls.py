from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from user.models import Post

urlpatterns = [
    url(r'^', ListView.as_view(queryset=Post.objects.all().order_by("-post_date")[:25], template_name="blog/index.html"))
]