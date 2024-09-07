from django.contrib import admin
from .models import UserProfile, Language, Country, Subscription


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('type', 'discount')
    search_fields = ('type',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number',
                    'reward_point', 'subscription_model', 'country', 'language')
    search_fields = ('user__username', 'address', 'phone_number')
    list_filter = ('subscription_model', 'country', 'language')
    readonly_fields = ('user',)  # Optionally make the user field read-only
    # If you want to allow image uploads in the admin panel, ensure that you configure MEDIA settings correctly

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ('user',) + self.readonly_fields
        return self.readonly_fields
