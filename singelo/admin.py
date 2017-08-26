from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude = ('post_slug',)
    list_display = (
        'post_title',
        'post_author',
        'post_created',
        'post_slug',
        'post_status'
    )

admin.site.register(Post, PostAdmin)
