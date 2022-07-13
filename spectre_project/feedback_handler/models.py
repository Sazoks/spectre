from django.db import models


class ContactDetails(models.Model):
    """
    Модель контактных данных клиента.

    Хранит в себе имя клиента, номер телефона, а также дату подачи заявления.
    Клиент может подать несколько заявок, так что делать поле номера телефона
    уникальным нет смысла.
    """

    client_name = models.CharField(max_length=64, verbose_name='Имя клиента')
    phone_number = models.CharField(max_length=32, verbose_name='Номер телефона',
                                    unique=True)
    date_application = models.DateTimeField(auto_now_add=True, db_index=True,
                                            verbose_name='Дата подачи заявления')

    class Meta:
        verbose_name_plural = 'Контактные данные'
        verbose_name = 'Контактные данные'
        ordering = ['date_application']

    def __str__(self):
        return f'{self.phone_number} {self.client_name}'


class SubscribeToNews(models.Model):
    """Модель подписки на рассылку"""

    client_email = models.EmailField(max_length=64, verbose_name='Электронная почта',
                                     unique=True)

    class Meta:
        verbose_name_plural = 'Подписки на рассылку'
        verbose_name = 'Подписка на рассылку'

    def __str__(self):
        return self.client_email
