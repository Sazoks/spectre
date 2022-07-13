from django.urls import path

from base_app.views import (
    index,
    services,
    about,
    contacts
)


urlpatterns = [
    path('', index, name='index'),
    path('services/<int:service_id>/', services, name='service'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
