from django.contrib import admin

# Register your models here.

from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    title_list = ['title']
    search_fields = ['content','id','title']

admin.site.register(Articles,ArticleAdmin)