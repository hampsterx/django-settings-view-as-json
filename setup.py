# -*- coding: utf-8 -*-

import os
import codecs
import re

from setuptools import setup, find_packages
from pip.req import parse_requirements


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='django-settings-view-as-json',
    version=find_version('django-settings-view-as-json', '__init__.py'),
    url='https://github.com/hampsterx/django-settings-view-as-json',
    install_requires=[str(ir.req) for ir in parse_requirements('requirements.txt')],
    packages=find_packages(),
    include_package_data=True,
    author='Tim van der Hulst',
    author_email='tim.vdh@gmail.com',
    license=read('LICENSE'),
    long_description=read('README.md'),
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
