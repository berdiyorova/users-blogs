from django.contrib import admin

from blogs.models import BlogModel


@admin.register(BlogModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
