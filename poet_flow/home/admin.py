from typing import Any
from django.contrib import admin
from .models import *


class PoetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display
    filter_horizontal = ['poems']
    prepopulated_fields = {'slug': ['name']}

class PoemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_author', 'poet_author', 'title', 'date']
    list_display_links = list_display
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ['title']}

    def save_model(self, request, obj, form, change):
        obj.save() 
        if obj.poet_author:
            obj.poet_author.poems.add(obj)


class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    list_display_links = list_display
    prepopulated_fields = {'slug': ['tag']}


admin.site.register(Poet, PoetAdmin)
admin.site.register(Poem, PoemAdmin)
admin.site.register(Tags, TagsAdmin)