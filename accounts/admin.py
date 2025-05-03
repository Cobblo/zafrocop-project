from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

# Custom admin for Account model
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Custom admin for UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_pic_thumbnail', 'user', 'city', 'state', 'country')

    def profile_pic_thumbnail(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.profile_picture.url
            )
        return '-'
    profile_pic_thumbnail.short_description = 'Profile Picture'

# Register models
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
