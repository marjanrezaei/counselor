from django.contrib import admin
from blog.models import Post,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display =('title', 'author', 'status', 'published_date', 'content_view')
    empty_value_dispaly = '-empty-'
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)