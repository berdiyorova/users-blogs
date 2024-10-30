from django.db import models

from common.models import BaseModel


class UserModel(BaseModel):
    full_name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', default='default_profile_pic.png')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-id',)
        db_table = 'user'
