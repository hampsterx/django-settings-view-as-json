# -*- coding: utf-8 -*-

import os
import codecs
import uuid

from setuptools import setup
from pip.req import parse_requirements

def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()

setup(
    name='django-settings-view-as-json',
    author='Tim van der Hulst',
    author_email='tim.vdh@gmail.com',
    version='0.0.3',
    url='https://github.com/hampsterx/django-settings-view-as-json',
    install_requires=[str(ir.req) for ir in parse_requirements('requirements.txt', session=uuid.uuid4())],
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
