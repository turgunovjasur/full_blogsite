from django.shortcuts import render
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.published.all()
