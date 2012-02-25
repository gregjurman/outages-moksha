# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, tmpl_context

from outages.lib.base import BaseController

from outages.decorators import with_moksha_socket

import moksha.utils

__all__ = ['RootController']

from moksha.api.widgets.live import LiveWidget
from tw2.polymaps import PolyMap

from tw2.dyntext import DynamicTextWidget

class DynamicTextLiveWidget(LiveWidget, DynamicTextWidget):
    onmessage = "setDynamicText('${id}', json.text)"

    resources = LiveWidget.resources + DynamicTextWidget.resources

class OutageMapWidget(LiveWidget, PolyMap):
    topic="map_geojson"

    onmessage = "addGeoJsonToPolymap('${id}', json, null)"

    center_latlon = {'lat': 43.105556, 'lon' : -76.611389}
    zoom = 6

    interact = True
    hash = True
    cloudmade_api_key = "1a1b06b230af4efdbb989ea99e9841af"

    # To style the map tiles
    cloudmade_tileset = 'midnight-commander'

    resources = LiveWidget.resources + PolyMap.resources


class RootController(BaseController):
    """
    The root controller for the outages application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    @expose('outages.templates.index')
    @with_moksha_socket
    def index(self):
        """Handle the front-page."""
        return dict(outage_map = OutageMapWidget, 
            outage_count=DynamicTextLiveWidget(topic="stat_outages", id="outage_count"),
            affected_count=DynamicTextLiveWidget(topic="stat_affected", id="affected_count"),
        )
