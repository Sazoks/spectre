from django.http import JsonResponse

from feedback_handler.models import (
    ContactDetails,
    SubscribeToNews,
)


def application(request):
    """Обработчик формы заявки"""

    if request.method == 'POST':
        client_name = request.POST.get('name', None)
        phone_number = request.POST.get('phone', None)

        # Проверка на валидность данных.
        if client_name is None or phone_number is None:
            return JsonResponse({'msg': 'No data available'}, status=400)
        if ContactDetails.objects.filter(phone_number=phone_number).first() is not None:
            return JsonResponse({'msg': 'The phone number already exists'}, status=403)

        ContactDetails.objects.create(client_name=client_name,
                                      phone_number=phone_number)

        return JsonResponse({'msg': 'OK'}, status=201)


def subscribe_to_news(request):
    """Обработчик формы подписки на рассылку"""

    if request.method == 'POST':
        client_email = request.POST.get('email', None)

        # Проверка на валидность данных.
        if client_email is None:
            return JsonResponse({'msg': 'No data available'}, status=400)
        if SubscribeToNews.objects.filter(client_email=client_email).first() is not None:
            return JsonResponse({'msg': 'Email already exists'}, status=403)

        SubscribeToNews.objects.create(client_email=client_email)

        return JsonResponse({'msg': 'OK'}, status=201)
