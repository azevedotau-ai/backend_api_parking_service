from django.contrib import admin
from .models import Vehicle, VehicleType

# Register your models here.

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','created_at')
    search_fields = ['name']
    list_filter = ('created_at',)
    ordering = ('created_at',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'brand', 'model','color', 'created_at')
    search_fields = ['license_plate','model']
    list_filter = ('vehicle_type',)
    ordering = ('created_at',)