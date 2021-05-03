from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

from django.contrib.admin import AdminSite


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.site_header = "Himanshu Sharma Blogs"
admin.site.site_title = "Himanshu Sharma Admin Panel"
