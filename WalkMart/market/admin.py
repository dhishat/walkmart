from django.contrib import admin

# Register your models here.
from .models import *


class MarketAdmin(admin.ModelAdmin):
    list_to_display = ('ID', 'Name', 'DbName', 'ConnectionString')


admin.site.register(WM_Market, MarketAdmin)
admin.site.register(WM_MarketPropertyDataElements)
admin.site.register(WM_MarketPropertyData)

