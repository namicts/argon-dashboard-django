from django import template
import os

register = template.Library()

@register.simple_tag
def company_brand():
    return os.environ.get('COMPANY_BRAND', 'ICTS')