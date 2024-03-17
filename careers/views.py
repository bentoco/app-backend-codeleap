from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CareerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.order_by("-created_datetime")
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'title': request.data.get('title'),
            'content': request.data.get('content')
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CareerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def patch(self, request, *args, **kwargs):
        post_entity = self.get_object()

        if not post_entity:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content')
        }
        serializer = PostSerializer(instance=post_entity, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post_entity = self.get_object()
        if not post_entity:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post_entity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
