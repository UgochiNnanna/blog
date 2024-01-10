from django.contrib import admin
from blog_app.models import Post, Comment, Reel

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_created',
        'date_updated'
    )
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Reel)