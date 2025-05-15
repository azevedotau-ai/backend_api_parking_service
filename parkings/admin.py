from django.contrib import admin
from .models import ParkingSpot, ParkingRecord


# Register your models here.
@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):

    list_display = ('spot_number', 'is_occupied','created_at')
    search_fields = ['spot_number']
    list_filter = ('created_at',)
    ordering = ('created_at',)


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):

    list_display = ('vehicle', 'parking_spot', 'entry_time','exit_time', 'created_at')
    search_fields = ('vehicle__license_plate','parking_spot__spot_number')
    ordering = ('created_at',)


    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "parking_spot" and not request.resolver_match.url_name.endswith('change'):
            kwargs['queryset'] = ParkingSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)