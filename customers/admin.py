from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bilheteIdentidade', 'phone', 'created_at')
    search_fields = ('name', 'bilheteIdentidade')
    list_filter = ('created_at',)
    ordering = ('created_at',)