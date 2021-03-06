# -*- coding: utf-8 -*-
"""`anarchytools` lives on `Github`_.

.. _github: https://github.com/AnarchyTools/anarchy_sphinx

"""
from setuptools import setup
from anarchy_theme import __version__


setup(
    name='anarchy_sphinx',
    version=__version__,
    url='https://github.com/AnarchyTools/anarchy_sphinx',
    license='BSD',
    author='Johannes Schriewer',
    author_email='hallo@dunkelstern.de',
    description='AnarchyTools Theme and Swift support for Sphinx.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['anarchy_theme', 'swift_domain'],
    package_data={
        'anarchy_theme': [
            'theme.conf',
            '*.html',
            'static/css/*.css'
        ]
    },
    entry_points={
        'console_scripts': [
            'anarchysphinx=swift_domain.bootstrap:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    install_requires=[
        'fuzzywuzzy',
        'sphinx'
    ]
)
