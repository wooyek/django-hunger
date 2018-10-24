#!/usr/bin/env python
from __future__ import unicode_literals

import pathlib
import sys

from django.conf import settings

BASE_DIR = pathlib.Path(__file__).absolute().parent

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'TEST_NAME': 'hunger_tests.db',
            },
        },
        DATABASE_NAME='test_hunger',
        TEST_DATABASE_NAME='hunger_tests.db',
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.contenttypes',
            'django_hunger2',
            'tests',
        ],
        ROOT_URLCONF='tests.urls',
        DEBUG=False,
        SITE_ID=1,
        TEMPLATES=[
            {
                # https://docs.djangoproject.com/en/1.8/topics/templates/#django.template.backends.django.DjangoTemplates
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    str(BASE_DIR / 'tests' / 'templates'),
                    str(BASE_DIR / 'example' / 'example' / 'templates'),
                ],
                # 'APP_DIRS': False, # APP_DIRS=True and loaders are conflicting
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                    'loaders': [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ],
                },
            },
        ],
        MIDDLEWARE=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django_hunger2.middleware.BetaMiddleware'
        ),
        HUNGER_REDIRECT='rejection',
        HUNGER_ALWAYS_ALLOW_VIEWS=[
            'tests.views.always_allow',
            'tests.views.rejection',
        ],
        HUNGER_ALWAYS_ALLOW_MODULES=['tests.always_allow_views'],
    )


def runtests():
    from django import setup
    setup()
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
