from django import template
from business.models import Course

register = template.Library()

@register.inclusion_tag('menu.html')
def menu():
    coursed = Course.objects.order_by('?')[:10]
    return {'coursed':coursed}