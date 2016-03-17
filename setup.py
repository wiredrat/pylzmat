#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension


lzmat_ext = Extension(
    'lzmat',
    sources=['src/lzmat/lzmat_dec.c', 'src/lzmat/lzmat_enc.c'])

setup(
    name='pylzmat',
    version='1.0',
    description='lzmat bindings.',
    author='Marcos Agüero',
    author_email='wiredrat@gmail.com',
    url='https://github.com/wiredrat/pylzmat',
    download_url='https://github.com/wiredrat/pylzmat/archive/1.0.tar.gz',
    py_modules=['pylzmat'],
    long_description='''
        Bindings for lzmat library (https://github.com/nemequ/lzmat).
''',
    ext_modules=[lzmat_ext],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
