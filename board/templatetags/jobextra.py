import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def convert_markdown(value):
    return markdown.markdown(value)


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)