from django.urls import path

from blogs.views import blogs, comments

app_name = 'blogs'

urlpatterns = [
    path('', blogs.blogs_list_create_view, name='blogs_list_create'),
    path('<int:pk>/', blogs.blog_detail, name='blog_detail'),
    path('comments/', comments.comments_list_create_view, name='comments_list_create'),
    path('comments/<int:pk>/', comments.comment_detail, name='comment_detail'),
]
