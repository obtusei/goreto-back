# admin.py
from .models import Alert, LocalAuthority
from django.contrib import admin
from .models import Alert


class AlertAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('user', 'latitude', 'longitude', 'problem',
                    'trail', 'created_at', 'last_modified')

    # Add filters to the sidebar
    list_filter = ('created_at', 'trail')

    # Add search functionality
    search_fields = ('user__username', 'problem', 'latitude', 'longitude')

    # Define fields to display in the detail view
    # fields = ('user', 'latitude', 'longitude', 'problem',
    #           'trail', 'created_at', 'last_modified')

    # Define which fields are readonly
    readonly_fields = ('created_at', 'last_modified')

    # Optional: Define fieldsets to group fields in the form
    fieldsets = (
        (None, {
            'fields': ('user', 'latitude', 'longitude', 'problem', 'trail')
        }),
        ('Date Information', {
            'fields': ('created_at', 'last_modified'),
            'classes': ('collapse',),
        }),
    )


# Register the model and the admin class
admin.site.register(Alert, AlertAdmin)


# admin.py


# class AlertAdmin(admin.ModelAdmin):
#     list_display = ('user', 'latitude', 'longitude', 'problem', 'trail', 'created_at', 'last_modified')
#     search_fields = ('user__username', 'problem', 'trail__name')
#     list_filter = ('created_at', 'trail')
#     readonly_fields = ('created_at', 'last_modified')
#     ordering = ('-created_at',)


class LocalAuthorityAdmin(admin.ModelAdmin):
    list_display = ('description', 'phone_number',
                    'email', 'latitude', 'longitude')
    search_fields = ('description', 'phone_number', 'email')
    list_filter = ('description',)
    # readonly_fields = ('latitude', 'longitude')
    ordering = ('description',)


# admin.site.register(Alert, AlertAdmin)
admin.site.register(LocalAuthority, LocalAuthorityAdmin)
