from django.contrib import admin
# Register your models here.
from markdownx.admin import MarkdownxModelAdmin

from .models import Post

admin.site.register(Post, MarkdownxModelAdmin)

#class BlogPostAdmin(MarkdownxModelAdmin) allows you to edit what is displayed when you are viewing the entries in admin and it inherits from MarkdownxModelAdmin so we can see the live preview.
class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created_date', 'mod_date')
    list_filter = ('created_date', 'mod_date')
    search_fields = ('title',)