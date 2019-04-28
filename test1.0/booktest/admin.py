from django.contrib import admin
from .models import *

# Register your models here.

# class HeroInfoInline(admin.TabularInline):
#     modle = HeroInfo
#     extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub']
    list_filter = ['btitle']
    search_fields = ['btitle']
    fieldsets = [
        ('base', {'fields':['btitle']}),
        ('super', {'fields':['bpub']})
    ]
    # inlines = [HeroInfoInline]



admin.site.register(Bookinfo, BookInfoAdmin)
admin.site.register(HeroInfo)