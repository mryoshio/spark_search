from django import template

register = template.Library()

@register.filter
def attr(value, attr=None):
    if attr is None: raise Exception('attr must not be None!')
    return getattr(value, attr)
