from django.contrib import admin
from .models import Task, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'slug', 'publish')
    search_fields = ('title', 'task')
    prepopulated_fields = {'slug': ['publish'], }
    date_hierarchy = 'publish'


admin.site.register(Task, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
