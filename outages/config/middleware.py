# -*- coding: utf-8 -*-
"""WSGI middleware initialization for the outages application."""

from outages.config.app_cfg import base_config
from outages.config.environment import load_environment

from moksha.middleware import make_moksha_middleware

__all__ = ['make_app']

# Use base_config to setup the necessary PasteDeploy application factory. 
# make_base_app will wrap the TG2 app with all the middleware it needs. 
make_base_app = base_config.setup_tg_wsgi_app(load_environment)


def make_app(global_conf, full_stack=True, **app_conf):
    """
    Set outages up with the settings found in the PasteDeploy configuration
    file used.
    
    :param global_conf: The global settings for outages (those
        defined under the ``[DEFAULT]`` section).
    :type global_conf: dict
    :param full_stack: Should the whole TG2 stack be set up?
    :type full_stack: str or bool
    :return: The outages application with all the relevant middleware
        loaded.
    
    This is the PasteDeploy factory for the outages application.
    
    ``app_conf`` contains all the application-specific settings (those defined
    under ``[app:main]``.
    
   
    """
    app = make_base_app(global_conf, full_stack=True, wrap_app=make_moksha_middleware, **app_conf)
    
    # Wrap your base TurboGears 2 application with custom middleware here
    
    return app
