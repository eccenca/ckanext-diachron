# coding: utf-8

import os
import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)

def package_read(context, data_dict=None):
    # Get the user name of the logged-in user.
    user_name = context['user']
    
    # We have the logged-in user's user name, get their user id.
    convert_user_name_or_id_to_id = toolkit.get_converter(
        'convert_user_name_or_id_to_id')
    try:
        user_id = convert_user_name_or_id_to_id(user_name, context)
    except toolkit.Invalid:
        # The user doesn't exist (e.g. they're not logged-in).
        return {'success': False,
                'msg': 'You must be logged-in as a member of the curators '
                       'group to create new groups.'}
    
    return {'success': True, 'msg': 'You are logged in, good.'}

def site_read(context, data_dict=None):
    # Get the user name of the logged-in user.
    user_name = context['user']
    
    # We have the logged-in user's user name, get their user id.
    convert_user_name_or_id_to_id = toolkit.get_converter(
        'convert_user_name_or_id_to_id')
    try:
        user_id = convert_user_name_or_id_to_id(user_name, context)
    except toolkit.Invalid:
        # The user doesn't exist (e.g. they're not logged-in).
        return {'success': False,
                'msg': 'You must be logged-in as a member of the curators '
                       'group to create new groups.'}
    
    return {'success': True, 'msg': 'You are logged in, good.'}

class DiachronPlugin(plugins.SingletonPlugin):
    
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IAuthFunctions)
    
    def update_config(self, config):  
        our_public_dir = os.path.join('theme', 'public')
        template_dir = os.path.join('theme', 'templates')

        # overriding configuration fields:
        # set our local template and resource overrides
        toolkit.add_public_directory(config, our_public_dir)
        toolkit.add_template_directory(config, template_dir)
        
        config['ckan.site_title'] = "Diachron Data Repository"
        config['ckan.site_logo'] = "/base/images/diachron_logo.png"

    def get_auth_functions(self):
        return {
            'site_read': site_read,
            'package_read': package_read
        }