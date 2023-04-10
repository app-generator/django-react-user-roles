from django.contrib import admin
from apps.home.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'address', 'phone', 'role',)
    list_filter = ('phone', 'role',)
    search_fields = ('phone', )

admin.site.register(UserProfile, UserProfileAdmin)