from django.db import models


# FIXME: Придумать нормальный способ получения пути
# FIXME: до картинок в шаблонах. Нужно избавиться от 'base_app/static/'.


class Service(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название услуги')
    image = models.ImageField(upload_to='base_app/static/base_app/img/services/service',
                              verbose_name='Изображение услуги')
    short_description = models.TextField(verbose_name='Краткое описание', null=True)

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услуга'

    def get_image(self):
        """
        Метод получения пути до изображения для шаблонов.
        Получаем путь до изображения относительно папки static
        приложения, в котором находится эта модель.
        """
        path_to_image = '/'.join(str(self.image).split('/')[2:])
        return path_to_image

    def __str__(self):
        return self.name


class ServiceSubsection(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название подраздела')
    description = models.TextField(verbose_name='Описание подраздела')
    image = models.ImageField(upload_to='base_app/static/base_app/img/services/service_subsection',
                              verbose_name='Изображение подраздела услуги')
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE,
                                verbose_name="Услуга")

    class Meta:
        verbose_name_plural = 'Подразделы услуг'
        verbose_name = 'Подраздел услуги'

    def get_image(self):
        """
        Метод получения пути до изображения для шаблонов.
        Получаем путь до изображения относительно папки static
        приложения, в котором находится эта модель.
        """
        path_to_image = '/'.join(str(self.image).split('/')[2:])
        return path_to_image

    def __str__(self):
        return self.name


class ItemFAQ(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    description_1 = models.TextField(verbose_name='Первая часть описания')
    description_2 = models.TextField(verbose_name='Вторая часть описания')
    image_1 = models.ImageField(upload_to='base_app/static/base_app/img/FAQ',
                                verbose_name='Первое изображение')
    image_2 = models.ImageField(upload_to='base_app/static/base_app/img/FAQ',
                                verbose_name='Второе изображение')

    class Meta:
        verbose_name_plural = 'Часто задаваемые вопросы'
        verbose_name = 'Вопрос'

    def get_image_1(self):
        """
        Метод получения пути до изображения для шаблонов.
        Получаем путь до изображения относительно папки static
        приложения, в котором находится эта модель.
        """
        path_to_image = '/'.join(str(self.image_1).split('/')[2:])
        return path_to_image

    def get_image_2(self):
        """
        Метод получения пути до изображения для шаблонов.
        Получаем путь до изображения относительно папки static
        приложения, в котором находится эта модель.
        """
        path_to_image = '/'.join(str(self.image_2).split('/')[2:])
        return path_to_image

    def __str__(self):
        return self.title
