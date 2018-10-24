#!/usr/bin/env python
from setuptools import setup, find_packages

DESCRIPTION = "A Django app to manage a private beta phase."

try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

INSTALL_REQUIRES = ['']
try:
    import importlib  # pylint: disable=unused-import
except ImportError:
    INSTALL_REQUIRES.append('importlib')

TESTS_REQUIRE = [
    'Django>=2.0',
]

setup(
    name='django-hunger2',
    version='2.2.0',
    packages=find_packages(exclude=['tests', 'example']),
    author='Joshua Karjala-Svenden',
    author_email='joshua@fluxuries.com',
    url='https://github.com/joshuakarjala/django-hunger/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={'test': TESTS_REQUIRE},
    test_suite='runtests.runtests',
    include_package_data=True,
)
