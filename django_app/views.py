from django.shortcuts import render


def menu_list(request):
    return render(request, 'django_app/menu_list.html', {})

