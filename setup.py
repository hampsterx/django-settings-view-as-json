# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='django-settings-view-as-json',
    author='Tim van der Hulst',
    author_email='tim.vdh@gmail.com',
    version='0.0.9',
    url='https://github.com/hampsterx/django-settings-view-as-json',
    install_requires=[
        "Django",
        "django-braces",
        "six",
    ],
    py_modules=['django_settings_view_as_json'],
    license=read('LICENSE'),
    description='View Django Settings at a URL',
    long_description=read('README.md'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
