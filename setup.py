#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-editor_access
# Created by Devoteam for Governo regional dos Azores

import setuptools

if __name__ == '__main__':
    setuptools.setup(
    name='ckanext-editor_access',
    version=1.0,
    description="Easy, CKAN  editor restrictions",
    long_description="""
    This CKAN extension provides a way to restrict editor role to delete anything thats is not owned by him
    """,
    keywords='ckan',
    author='Martim',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'ckanapi',
        'ckantoolkit>=0.0.7',
    ],
    entry_points='''
    [ckan.plugins]
    editor_access=ckanext.editor_access.plugin:UserDatasetsPlugin
    '''
)
