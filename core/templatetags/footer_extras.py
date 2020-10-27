from django import template
import os

register = template.Library()

@register.simple_tag
def company_link():
    return os.environ.get('COMPANY_LINK', '#')

@register.simple_tag
def company_name():
    return os.environ.get('COMPANY_NAME', 'ICTS')

@register.simple_tag
def copyright():
    return os.environ.get('COPYRIGHT', 'ICTS')

@register.simple_tag
def coded_by():
    return os.environ.get('CODED_BY', 'ICTS')