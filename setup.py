#!/usr/bin/env python3

from setuptools import setup


setup(
    name='repology-export',
    version='0.0.0',
    description='Collection of exports for Repology project',
    author='Dmitry Marakasov',
    author_email='amdmi3@amdmi3.ru',
    url='https://repology.org/',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=[
        'repologyexport',
    ],
    scripts=[
        'repology-export.py',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=">=3.6",
    install_requires=[
        'psycopg2>=2.8.3',
    ]
)
