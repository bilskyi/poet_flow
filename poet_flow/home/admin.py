from django.contrib import admin
from .models import *

class PoemAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date']
    prepopulated_fields = {'slug': ['title']}


class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']
    prepopulated_fields = {'slug': ['tag']}


admin.site.register(Poem, PoemAdmin)
admin.site.register(Tags, TagsAdmin)