from django.contrib import admin
from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'is_published', 'list_date', 'price', 'realtor'
    )
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)