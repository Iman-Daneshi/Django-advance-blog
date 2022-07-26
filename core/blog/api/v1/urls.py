from django.urls import path, include
from .views import (  # post_list,
    # post_detail,
    # PostList,
    # PostDetail,
    PostModelViewSet,
    CategoryModelViewSet,
)
from rest_framework.routers import DefaultRouter


app_name = "api-v1"

router = DefaultRouter()
router.register("post", PostModelViewSet, basename="post")
router.register("category", CategoryModelViewSet, basename="category")
urlpatterns = router.urls

# urlpatterns = [
#     #path('post/', post_list, name='post-list'),
#     #path('post/<int:id>', post_detail, name='post-detail'),
#     # path('post/', PostList.as_view(), name='post-list'),
#     # path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
#     path('post/', PostViewSet.as_view({'get':'list', 'post':'create'}), name='post-list'),
#     path('post/<int:pk>/', PostViewSet.as_view({'get':'retrieve', 'put':'update','patch':'partial_update', 'delete':'destroy' }), name='post-detail'),
# ]
