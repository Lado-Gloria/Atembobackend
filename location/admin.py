from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('username', 'region_name', 'phone_number', 'installation_date', 'status', 'updated_at')
    list_filter = ('installation_date', 'updated_at')
    search_fields = ('region_name', 'username', 'phone_number')

admin.site.register(Location, LocationAdmin)
