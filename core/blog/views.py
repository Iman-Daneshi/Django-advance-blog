from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from .models import Post

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ali'
        context['posts'] = Post.objects.all()
        return context


class RedirectToMaktabkhooneh(RedirectView):
    url = 'http://maktabkhooneh.org/'


class RedirectToindex(RedirectView):
    pattern_name = 'blog:index'

class PostListView(ListView):
    queryset = Post.objects.filter(status=1)
    # model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'post_list'
    ordering = '-published_date'
    paginate_by = 2
    

    # def get_queryset(self):  # = model= queryset
    #     posts = Post.objects.filter(status=1)
    #     return posts
    
