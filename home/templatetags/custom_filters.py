from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Splits a string by the given separator.
    Usage in template: {{ value|split:"," }}
    """
    if value:
        return value.split(arg)
    return []
