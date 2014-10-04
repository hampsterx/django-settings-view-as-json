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
            for item in val:
                if isinstance(item, dict):
                    serialize_function_values(item)

            continue

        the_dict[key] = "{} ({})".format(unicode(val), val.__class__.__name__)


class settings_view(JSONResponseMixin, View):

    json_dumps_kwargs = {u"indent": 2}

    def get(self, request, *args, **kwargs):

        from django.conf import settings
        data = dict()

        for k in dir(settings):
            if k.isupper():
                data[k] = getattr(settings, k)

        null_key_values(data, "password")
        null_key_values(data, "secret")
        null_key_values(data, "key")

        serialize_function_values(data)

        return self.render_json_response({u"settings": data})
