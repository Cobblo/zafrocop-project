from django import template

register = template.Library()

@register.filter
def stars_range(arg):
    return range(10, 0, -1)

@register.filter
def adjust(value):
    return (int(value) - 1) / 2

@register.filter
def make_range(start, end):
    return range(start, end + 1)
