from django.contrib import admin
from boke.models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title','category','created','modified'
    ]
    search_fields = ['title']
    list_per_page = 10
    list_filter = ['title']
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']