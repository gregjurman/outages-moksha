# -*- coding: utf-8 -*-
"""Setup the outages application"""

import logging
from tg import config
from outages import model
import transaction

def bootstrap(command, conf, vars):
    """Place any commands to setup outages here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
