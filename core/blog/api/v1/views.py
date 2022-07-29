from rest_framework.permissions import (
    IsAuthenticated,
    # IsAdminUser,
    IsAuthenticatedOrReadOnly,
    # IsAdminUser,
)

# from rest_framework.generics import (
#     GenericAPIView,
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# from rest_framework import mixins
# from rest_framework import status
# from rest_framework.views import APIView
from rest_framework import viewsets

from ...models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination
# from .filters import PostFilters

"""
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""

"""@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostSerializer(post, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        post.delete()
        return Response({'detail':'The post is removed'}, status=status.HTTP_204_NO_CONTENT)"""

"""
class PostList(APIView):
    ''' Getting a list of posts and creating new post'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        '''reteiveing a list of posts'''
        posts = Post.objects.filter(status=True)
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''creating a new post using given data'''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""


"""create a custom Postlist view
class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin  ):
    ''' Getting a list of posts and creating new post'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create (request, *args, **kwargs)
        """

"""
class PostDetail(APIView):
    ''' a class for displaying, updating, and editing a single post '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        '''reteiveing a single post'''
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail': 'The post is removed'}, status=status.HTTP_204_NO_CONTENT)
"""

"""class PostList(ListCreateAPIView):
    ''' Getting a list of posts and creating new post'''
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    ''' a class for displaying, updating, and editing a single post '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
"""

"""
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.filter(status=True)
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data)

    def create(self, request):
        #queryset = Post.objects.filter(status=True)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post_object = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post_object = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Post.objects.filter(status=True)
        post_object = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        #queryset = Post.objects.filter(status=True)
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({'detail': 'The post is removed'}, status=status.HTTP_204_NO_CONTENT)
"""


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {"category": ["exact"], "author": ["exact"], "status": ["exact"]}
    # filterset_class = PostFilters
    # '$' is a Regex search: showing similar things to what user has searched
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination

    # @action(methods=["get"], detail=False)
    # def get_ok(self, request):
    #     return Response({"detail": "Ok"})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
