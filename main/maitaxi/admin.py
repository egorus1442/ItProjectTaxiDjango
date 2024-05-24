from django.contrib import admin
from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'experience', 'car', 'car_id', 'rating', 'col_review')
