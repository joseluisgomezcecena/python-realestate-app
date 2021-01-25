from django.contrib import admin
from .models import Listing
from django.utils.html import format_html

class listingAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))
    
    image_tag.short_description = 'photo_main'



    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'photo_main')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'zip_code', 'address', 'city', 'state')
    list_per_page = 25

admin.site.register(Listing, listingAdmin)

# Register your models here.
