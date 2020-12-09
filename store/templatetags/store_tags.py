from django import template

register = template.Library()


@register.filter
def get_quantity(dictionary, key):
    try:
        return dictionary.get(str(key))['quantity']
    except KeyError:
        return str(1)
