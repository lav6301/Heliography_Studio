from django.contrib import admin
from .models import Service, ServiceImage

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage)
