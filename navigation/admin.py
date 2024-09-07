from django.contrib import admin
from .models import UserNavigation

@admin.register(UserNavigation)
class UserNavigationAdmin(admin.ModelAdmin):
    list_display = ('user', 'trail', 'current_coordinate', 'last_checkpoint')
    search_fields = ('user__username', 'trail__name', 'current_coordinate__latitude', 'last_checkpoint__name')
    list_filter = ('trail', 'last_checkpoint')
