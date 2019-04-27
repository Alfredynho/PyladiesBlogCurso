from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from apps.post.models import Post

class HomeView(TemplateView):

    template_name = "index.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        print("CONTEXT >> ", context)
        return context    