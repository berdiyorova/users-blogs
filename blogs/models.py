from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField

from common.models import BaseModel
from users.models import UserModel


class BlogModel(BaseModel):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    # description = models.RichTextUploadingField()

    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='blogs')

    def __str__(self):
        return f"{self.title} by {self.author.__str__()}"

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('-id',)
        db_table = 'blog'


class CommentModel(BaseModel):
    text = models.TextField()

    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='comments')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-id',)
        db_table = 'comment'
