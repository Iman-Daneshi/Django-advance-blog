from django.urls import path
from .views import (IndexView, RedirectToMaktabkhooneh, 
                    RedirectToindex, PostListView)


app_name = "blog"

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    # path('go-to-maktabkhooneh/', RedirectToMaktabkhooneh.as_view(),
    #      name='go-to-maktabkhooneh'),
    # path('go-to-index/', RedirectToindex.as_view(),
    #     name='go-to-index'),
    path('post/', PostListView.as_view(), name='post-list'),
]
