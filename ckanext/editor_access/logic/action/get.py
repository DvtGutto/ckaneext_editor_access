#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-editor_access
# Created by Devoteam for Governo regional dos Azores

from ckan.plugins import toolkit


@toolkit.chained_action
def organization_list_for_user(next_action, context, data_dict):
    '''
    :param next_action:
    :param context:
    :param data_dict:

    '''
    perm = data_dict.get('permission')
    if perm in ['create_dataset', 'update_dataset', 'delete_dataset']:
        # Create a copy of the data dict, and change the request permission to
        # 'read' which will be granted to all members of a group.
        data_dict = {**data_dict, **{'permission': 'read'}}

    return next_action(context, data_dict)
