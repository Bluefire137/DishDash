from django import template
import dishes.views as views

register = template.Library()

@register.simple_tag()
def get_types():
    return views.types_db
