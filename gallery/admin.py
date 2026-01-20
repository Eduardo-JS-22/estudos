from django.contrib import admin
from gallery.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'legend')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'legend')
    list_filter = ('id', 'name')

admin.site.register(Image, ImageAdmin)