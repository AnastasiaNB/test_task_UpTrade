import re

from django import template
from main_menu.models import Parent

register = template.Library()
child_page_pattern = re.compile('page-\d-\d')


@register.inclusion_tag('main_menu/main_menu.html')
def draw_menu(active=None):
    parents = Parent.objects.all()  # single request to database
    try:
        if child_page_pattern.match(active):  # for right representation of child pages
            index = active.find('-', 5)
            active = active[:index]
    except TypeError:
        pass
    menu = {
        "parents": parents,
        "active": active,
    }
    return menu
