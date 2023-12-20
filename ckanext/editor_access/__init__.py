#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-editor_access
# Created by Devoteam for Governo regional dos Azores

try:
    import pkg_resources

    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil

    __path__ = pkgutil.extend_path(__path__, __name__)
