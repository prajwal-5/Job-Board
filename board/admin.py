from django.contrib import admin
from .models import Job
# Register your models here.

@admin.register(Job)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'location', 'deadline', 'email', 'order']