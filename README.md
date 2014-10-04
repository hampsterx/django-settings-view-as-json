# django-settings-view-as-json

View Django Settings via URL

[![Latest PyPI version](https://pypip.in/v/django-settings-view-as-json/badge.png)](https://crate.io/packages/django-settings-view-as-json/)
[![Number of PyPI downloads](https://pypip.in/d/django-settings-view-as-json/badge.png)](https://crate.io/packages/django-settings-view-as-json/)

## Why

Because sometimes its confusing what settings are in use in your staging environments etc.

## Features

* Recursively nulls out any sensitive key values (eg passwords)

## Install

```python
pip install django-settings-view-as-json install
```

## Usage

```python
from django_settings_view_as_json import settings_view

url(r'^settings/$', settings_view.as_view(), name='settings'),
```

## Security Warning

I highly recommend limiting this URL to either non production environments or at least Super user's. Eg

```python
from django.contrib.auth.decorators import user_passes_test
from django_settings_view_as_json import settings_view

url(r'^settings/$', user_passes_test(lambda u: u.is_superuser)(settings_view.as_view()), name='settings'),

```

## TODO

* Make sensitive key list a setting

