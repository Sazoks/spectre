from django.urls import path

from feedback_handler.views import (
    application,
    subscribe_to_news,
)


urlpatterns = [
    path('application/', application, name='application'),
    path('subscribe_to_news/', subscribe_to_news, name='subscribe_to_news'),
]
