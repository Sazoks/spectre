from django.contrib import admin

from feedback_handler.models import (
    ContactDetails,
    SubscribeToNews,
)


class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'phone_number', 'date_application', )
    list_display_links = ('client_name', 'phone_number', )
    search_fields = ('client_name', 'phone_number', )


class SubscribeToNewsAdmin(admin.ModelAdmin):
    list_display = ('client_email', )
    list_display_links = ('client_email', )
    search_fields = ('client_email', )


admin.site.register(ContactDetails, ContactDetailsAdmin)
admin.site.register(SubscribeToNews, SubscribeToNewsAdmin)
