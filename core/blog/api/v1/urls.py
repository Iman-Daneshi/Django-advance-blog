from django.urls import path, include
from .views import post_list, post_detail


app_name = "blog"

urlpatterns = [
    path('post/', post_list, name='post-list'),
    path('post/<int:id>', post_detail, name='post-list'),
]
