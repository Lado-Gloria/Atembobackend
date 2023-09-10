from django.contrib import admin
from .models import Registration

# Register your models here.
class Registration_admin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","password")
admin.site.register(Registration,Registration_admin)