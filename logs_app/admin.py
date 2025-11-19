from django.contrib import admin
from .models import Profile, LogFile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "gender", "dob")
    search_fields = ("full_name", "user__username")

@admin.register(LogFile)
class LogFileAdmin(admin.ModelAdmin):
    list_display = ("file_name", "uploaded_by", "upload_time")
    search_fields = ("file_name", "uploaded_by__username")
    list_filter = ("upload_time",)
