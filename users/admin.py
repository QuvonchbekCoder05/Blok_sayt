from django.contrib import admin
from .models.user import User
from .models.otp import OTP

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_active', 'is_admin')
    search_fields = ('email', 'username')
    list_filter = ('is_active', 'is_admin')

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'otp_code', 'created_at', 'expires_at')
    search_fields = ('user__email',)
    list_filter = ('created_at',)
