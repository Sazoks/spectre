from django.contrib import admin

from base_app.models import (
    Service,
    ServiceSubsection,
    ItemFAQ,
)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class ServiceSubsectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'service', )
    list_display_links = ('name', 'description', 'service', )
    search_fields = ('name', 'service', )


class ItemFAQAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceSubsection, ServiceSubsectionAdmin)
admin.site.register(ItemFAQ, ItemFAQAdmin)
