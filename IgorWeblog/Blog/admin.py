from django.contrib import admin
from .models import Task


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'slug', 'publish')
    search_fields = ('title', 'task')
    prepopulated_fields = {'slug': ['publish'], }
    date_hierarchy = 'publish'


admin.site.register(Task, PostAdmin)
