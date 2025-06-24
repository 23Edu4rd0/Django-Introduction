from django.contrib import admin
from galeria.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'legend', 'photo', 'credits')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id',)
    
    
admin.site.register(Image, ImageAdmin)
