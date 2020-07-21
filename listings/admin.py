from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'is_published', 'list_date', 'price', 'realtor'
    )
    list_display_links = ('id', 'title')
    list_per_page = 25
    list_editable = ('is_published',)
    list_filter = ('realtor',)


admin.site.register(Listing, ListingAdmin)