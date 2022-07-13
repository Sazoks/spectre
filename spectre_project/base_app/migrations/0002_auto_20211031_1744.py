# Generated by Django 3.2.8 on 2021-10-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название услуги')),
                ('image', models.ImageField(upload_to='base_app/static/img/services/service', verbose_name='Изображение услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServiceSubsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название подраздела')),
                ('description', models.TextField(verbose_name='Описание подраздела')),
                ('image', models.ImageField(upload_to='base_app/static/img/services/service_subsection')),
            ],
            options={
                'verbose_name': 'Подраздел',
                'verbose_name_plural': 'Подразделы',
            },
        ),
        migrations.DeleteModel(
            name='ContactDetails',
        ),
        migrations.DeleteModel(
            name='SubscribeToNews',
        ),
        migrations.AddField(
            model_name='service',
            name='subsections',
            field=models.ManyToManyField(to='base_app.ServiceSubsection'),
        ),
    ]