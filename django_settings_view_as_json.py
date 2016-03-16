import copy

import inspect
from collections import OrderedDict
from django.views.generic import View
from braces.views import JSONResponseMixin


def null_key_values(the_dict, name):
    """
    Null Key Values
    if "name" in key then replace the value with None
    """
    for key, value in the_dict.items():
        if isinstance(key, basestring) and name.upper() in key.upper():
            the_dict[key] = None

        if isinstance(value, dict):
            null_key_values(value, name)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    null_key_values(item, name)


def serialize_function_values(the_dict):

    for key, val in the_dict.items():
        if val is None or isinstance(val, basestring) or isinstance(val, int) or isinstance(val, float):
            continue

        if isinstance(val, tuple):
            val = list(val)
            the_dict[key] = val

        if isinstance(val, dict):
            serialize_function_values(val)
            continue

        elif isinstance(val, list):
            for i, item in enumerate(val):
                if isinstance(item, dict):
                    serialize_function_values(item)
                elif inspect.isclass(item):
                    val[i] = repr(item)

            continue

        the_dict[key] = u"{} ({})".format(unicode(val), val.__class__.__name__)


class settings_view(JSONResponseMixin, View):

    json_dumps_kwargs = {u"indent": 2}

    def get(self, request, *args, **kwargs):

        from django.conf import settings
        data = OrderedDict()

        for k in dir(settings):
            if k.isupper():
                try:
                    data[k] = copy.deepcopy(getattr(settings, k))
                except:
                    try:
                        data[k] = copy.copy(getattr(settings, k))
                    except:
                        data[k] = getattr(settings, k).__class__.__name__

        null_key_values(data, "password")
        null_key_values(data, "secret")
        null_key_values(data, "key")

        serialize_function_values(data)

        return self.render_json_response({u"settings": data})
