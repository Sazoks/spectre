from django.shortcuts import render, get_object_or_404

from base_app.models import (
    Service,
    ItemFAQ,
)


def index(request):
    """Контроллер главной страницы"""

    all_services = Service.objects.all()
    all_faq = ItemFAQ.objects.all()
    context = {'services': all_services, 'FAQs': all_faq, }

    return render(request=request,
                  template_name='base_app/index.html',
                  context=context)


def services(request, service_id: int):
    """Контроллер шаблона услуг"""

    current_service = get_object_or_404(Service, pk=service_id)
    subsections = current_service.servicesubsection_set.all()
    all_services = Service.objects.all()
    context = {'services': all_services,
               'current_service': current_service,
               'subsections': subsections, }

    return render(request=request,
                  template_name='base_app/service.html',
                  context=context)


def about(request):
    """Контроллер шаблона информации о компании"""

    all_services = Service.objects.all()
    context = {'services': all_services, }

    return render(request=request,
                  template_name='base_app/about.html',
                  context=context)


def contacts(request):
    """Контроллер шаблона страницы контактов"""

    all_services = Service.objects.all()
    context = {'services': all_services, }

    return render(request=request,
                  template_name='base_app/contacts.html',
                  context=context)
