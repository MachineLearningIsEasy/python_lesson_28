from django.contrib import admin

from .models import Tag, Article

# admin.site.register(Tag)
# admin.site.register(Article)


def set_active(modeladmin, request, queryset):
    queryset.update(is_active = True)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_name','article_text', 'is_active','article_rating']
    actions = [set_active]

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name','is_active']
    actions = [set_active]

admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)