from tg import tmpl_context
import moksha.api.widgets
from tw2.jqplugins.ui import set_ui_theme_name

import decorator

def with_moksha_socket(f, *args, **kw):
    tmpl_context.moksha_socket = moksha.api.widgets.moksha_socket
    return f(*args, **kw)

def with_ui_theme(f, *args, **kw):
    set_ui_theme_name('hot-sneaks') # hell yes
    return f(*args, **kw)

with_moksha_socket = decorator.decorator(with_moksha_socket)
with_ui_theme = decorator.decorator(with_ui_theme)
