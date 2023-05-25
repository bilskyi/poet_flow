from django.contrib import admin
from .models import *


class PoetAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['poems']
    prepopulated_fields = {'slug': ['name']}

class PoemAdmin(admin.ModelAdmin):
    list_display = ['user_author', 'poet_author', 'title', 'date']
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ['title']}


class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']
    prepopulated_fields = {'slug': ['tag']}


admin.site.register(Poet, PoetAdmin)
admin.site.register(Poem, PoemAdmin)
admin.site.register(Tags, TagsAdmin)