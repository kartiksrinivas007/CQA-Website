from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def custom_filter(text, color):
    safe_text = '<span style="color:{color}">{text}</span>'.format(color=color, text=text)
    return mark_safe(safe_text)