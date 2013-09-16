# coding: utf-8

import os
import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def site_read(context, data_dict=None):
    return {'success': False, 'msg': 'No one is allowed to see anything'}

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
        return {'site_read': site_read}