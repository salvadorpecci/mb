from django.shortcuts import render

# Create your views here.
# posts/views.py
from django.views.generic import ListView # new
from .models import Post                  # new


class HomePageView(ListView):             # new
    model = Post                          # new
    template_name = 'home.html'           # new
    context_object_name = 'all_posts_list'          # new
