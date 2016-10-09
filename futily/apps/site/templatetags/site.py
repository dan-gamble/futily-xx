import json
import os
import urllib

import jinja2
from cms.apps.pages.templatetags.pages import _navigation_entries
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django_jinja import library


@library.global_function
@jinja2.contextfunction
def get_navigation_json(context, pages, section=None):
    return json.dumps(_navigation_entries(context, pages, section, is_json=True))


@library.global_function
def frontend_templates():
    return mark_safe([
        str(f[:-5])
        for f in os.listdir(os.path.join(settings.TEMPLATES[0]["DIRS"][0], 'frontend'))
        if f[:1] != '_'
    ])


@jinja2.contextfunction
@library.global_function
def url(context, *args, **kwargs):
    request = context['request']
    get = kwargs.pop('get', {})
    remove = kwargs.pop('remove', '')
    return_url = ''

    # Sometimes no 'viewname' is passed i.e. building pagination links
    if args or kwargs:
        return_url = reverse(*args, **kwargs)

    if hasattr(request.GET, 'dict'):
        params = request.GET.dict()

        # If we want to change something more than likely we want to
        # reset the current page, so remove the page param
        if 'page' in params and get:
            params.pop('page')

        if remove:
            for item in remove:
                params.pop(item, None)

        params.update(**get)

        return_url += '?{}'.format(urllib.urlencode(params))

    if return_url == '?':
        return request.path

    return return_url
