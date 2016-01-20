#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
]

if sys.version_info < (3, 2):
    requirements.append('contextdecorator')

test_requirements = [
]

setup(
    name='timeoutcontext',
    version='0.1.0',
    description="A signal based timeout context manager",
    long_description=readme + '\n\n' + history,
    author="Antoine Cezar",
    author_email='antoine@cezar.fr',
    url='https://github.com/AntoineCezar/timeoutcontext',
    packages=[
        'timeoutcontext',
    ],
    package_dir={'timeoutcontext':
                 'timeoutcontext'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='timeoutcontext',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
