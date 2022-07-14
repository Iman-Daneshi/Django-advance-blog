from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ...models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, id):
    # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({"detail":"Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
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
        return Response({'detail':'The post is removed'}, status=status.HTTP_204_NO_CONTENT)
