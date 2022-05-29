from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This will cut 'arg' from 'value' string
    """
    return value.replace(arg,"")

#register.filter('cut',cut)          # filterName, filterFunction
