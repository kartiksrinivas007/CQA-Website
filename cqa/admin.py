from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cqa.models import CustomUser

class CustomUserAdmin(UserAdmin):
    # list_display = ('account_id','username', 'display_name', 'reputation', 'views', 'down_votes', 'up_votes',
    #                 'location', 'profile_image_url', 'website_url', 'about_me', 'creation_date',
    #                  'is_active', 'is_staff', 'last_login')
    list_display = ('account_id','username', 'display_name', 'creation_date',
                     'is_active', 'is_staff', 'last_login')
    
    search_fields = ('account_id', 'username', 'display_name')
    readonly_fields = ('account_id', 'reputation', 'views', 'down_votes', 'up_votes',
                     'creation_date','is_active', 'is_staff', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)