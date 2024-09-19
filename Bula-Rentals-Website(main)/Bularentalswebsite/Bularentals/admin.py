from django.contrib import admin
from .models import Vehicles

@admin.register(Vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'status', 'daily_rate', 'brand', 'model')
    search_fields = ('license_plate', 'brand', 'model')
  
