# ckanext_editor_access


## Overview
This extension changes the permissions of users with the 'Editor' role in an organisation, allowing them to create datasets, and to edit or delete the datasets they have created and also edit datasets in organisation that they dont own but not delete.. Unlike users with the 'Admin' role, they cannot edit or delete datasets created by other users.

## Notes:

This applies to the existing 'Editor' role rather than creating a new one as it is currently not possible to add new roles from an extension;
The plugin works with custom dataset types, however it will not work with other plugins which override package/resource update/create/delete authorization functions, and package_create/update actions.

***Warning: This plugin modifies CKAN's permission system. The current implementation should only be used AT YOUR OWN RISK in a trusted environment. Ensure you run the tests with your plugins enabled.***


## Installation

1 - Clone this repository into  `/usr/lib/ckan/default/src`

 - `cd /usr/lib/ckan/default/src`
 - `git clone https://github.com/DvtGutto/ckanext-editor_access.git`


2 - Execute command into  `/usr/lib/ckan/default/src/ckanext-editor_access`

 - `cd /usr/lib/ckan/default/src/ckanext-editor_access`
 - `python setup.py develop`

3 - Add plugin into `ckan.ini`  file

  - `ckan.plugins = ... editor_access`
