from typing import Any
from django.contrib import admin
from .models import *


class PoetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display
    filter_horizontal = ['poems']
    prepopulated_fields = {'slug': ['name']}

class PoemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_display_links = list_display
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ['title']}


class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    list_display_links = list_display
    prepopulated_fields = {'slug': ['tag']}


admin.site.register(Poet, PoetAdmin)
admin.site.register(Poem, PoemAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(ClassicPoem)
admin.site.register(UserPoem)