from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from .models import Post
from .forms import PostForm

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

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'

'''
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''
class PostCreateView(CreateView):
    model = Post
    fields = ['author', 'title', 'content',
              'category', 'status', 'published_date'
              ]

    success_url = '/blog/post/'
