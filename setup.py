#!/usr/bin/env python

import os
import re

from setuptools import find_packages, setup


def get_long_description():
    for filename in ('README.rst',):
        with open(filename, 'r') as f:
            yield f.read()


def get_version(package):
    with open(os.path.join(package, '__init__.py')) as f:
        pattern = r'^__version__ = [\'"]([^\'"]*)[\'"]'
        return re.search(pattern, f.read(), re.MULTILINE).group(1)


setup(
    name='django-graphql-social-auth',
    version=get_version('graphql_social_auth'),
    license='MIT',
    description='Python Social Auth support for Django GraphQL',
    long_description='\n\n'.join(get_long_description()),
    author='mongkok',
    author_email='domake.io@gmail.com',
    maintainer='mongkok',
    url='https://github.com/flavors/django-graphql-social-auth/',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Django>=1.11',
        'django-filter>=1.1.0',
        'graphene-django>=2.0.0',
        'social-auth-app-django>=2.1.0',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
    ],
    zip_safe=False,
    tests_require=[
        'Django>=1.11',
        'django-filter>=1.1.0',
        'graphene-django>=2.0.0',
        'social-auth-app-django>=2.1.0',
    ],
    package_data={
        'graphql_social_auth': [
            'locale/*/LC_MESSAGES/django.po',
            'locale/*/LC_MESSAGES/django.mo',
        ],
    },
    extras_require={
        'jwt': ['django-graphql-jwt>=0.1.2'],
    },
)
