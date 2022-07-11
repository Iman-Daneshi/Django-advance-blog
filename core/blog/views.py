from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (ListView, DetailView, CreateView,
                                  UpdateView, DeleteView,)
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'blog.view_post'
    queryset = Post.objects.filter(status=1)
    # model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'post_list'
    ordering = '-published_date'
    paginate_by = 2
    

    # def get_queryset(self):  # = model= queryset
    #     posts = Post.objects.filter(status=1)
    #     return posts


class PostDetailView(LoginRequiredMixin, DetailView):
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


class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content',
    #           'category', 'status', 'published_date'
    #           ]
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'
