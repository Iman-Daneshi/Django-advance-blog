from django.urls import path
from .views import (IndexView, PostUpdateView, RedirectToMaktabkhooneh, Post, 
                    RedirectToindex, PostListView, PostDetailView, PostCreateView)


app_name = "blog"

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    # path('go-to-maktabkhooneh/', RedirectToMaktabkhooneh.as_view(),
    #      name='go-to-maktabkhooneh'),
    # path('go-to-index/', RedirectToindex.as_view(),
    #     name='go-to-index'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
]
