from django.contrib import admin
from .models import User, Train

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
    ]

@admin.register(Train)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'train_name',
        'source',
        'destination',
        'seat_capacity',
        'arrival_time_at_source',
        'arrival_time_at_destination'
    ]
