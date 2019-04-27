from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'autor',
        # 'image',
        'content',
        'publication_date',
        'status',
    )

    class Meta:
        model = Post
