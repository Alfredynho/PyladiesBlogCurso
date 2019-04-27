from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Post

class PostList(ListView):
	model = Post
	template_name = "blog.html"
	context_object_name = 'posts'
    
class DetailPost(DetailView):
	model = Post
	template_name = 'read.html'
	context_object_name = 'post'