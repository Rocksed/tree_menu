from django import template
from django_app.models import Menu

register = template.Library()


def get_menu_recursive(menu_items):
    result = []
    for item in menu_items:
        children = get_menu_recursive(item.children.all())
        result.append({
            'item': item,
            'children': children
        })
    return result


@register.inclusion_tag('django_app/menu.html')
def draw_menu(main_menu):
    main_menu_title = "Главное меню"
    main_menu = get_menu_recursive(Menu.objects.filter(parent_menu_item__isnull=True))
    return {'main_menu': main_menu, 'main_menu_title': main_menu_title}

