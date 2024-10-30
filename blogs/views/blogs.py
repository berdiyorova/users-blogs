from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blogs.models import BlogModel
from blogs.serializers import BlogSerializer
from users.models import UserModel


@api_view(['GET', 'POST'])
def blogs_list_create_view(request):
    if request.method == 'GET':
        blogs = BlogModel.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def blog_detail(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = BlogSerializer(instance=blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PATCH':
        serializer = BlogSerializer(instance=blog, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        blog.delete()
        return Response(data={'success': True}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_blogs(request, pk):
    blogs = BlogModel.objects.filter(author=UserModel.objects.get(pk=pk))
    if request.method == 'GET':
        serializer = BlogSerializer(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
