from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hire_date', 'email')
    list_display_links = ('id', 'name')
    list_per_page = 25
    list_filter = ('hire_date',)


admin.site.register(Realtor, RealtorAdmin)
