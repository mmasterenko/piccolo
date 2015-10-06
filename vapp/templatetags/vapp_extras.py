from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def x_active_class(context, url_name=None):
    result = ''
    request = context['request']
    request_path = request.path
    url_path = reverse(url_name)
    is_main = request_path == url_path
    is_other = request_path.find(url_path) > -1 and url_path != '/'
    if is_other or is_main:
        result = 'class="x-active"'
    return result
