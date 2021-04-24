from django.contrib import admin
from .models import User, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    model = User
    fieldsets = [
        ('User Credentials', {'fields': ['email', 'full_name', 'username', 'contact', 'password',]}),
        ('Status', {'fields': ['is_staff', 'is_superuser', 'is_active', ]}),
        ('User Permission Groups', {'fields':['groups']}),
        ('User Permissions', {'fields': ['user_permissions']}),
        ('More', {'fields': ['last_login', 'date_joined']}),
    ]

    list_display = ['id', 'username', 'email', 'full_name', 'is_staff',]
    list_filter = ['username','is_staff',]
    search_fields = ['username', 'is_staff',]
    list_display_links = ('id', 'username')

    inlines = [UserProfileInline]

admin.site.register(User, UserAdmin)

    
