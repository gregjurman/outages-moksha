from moksha.api.widgets.live import LiveWidget
from tw2.polymaps import PolyMap

import tw2.core as twc
import tw2.jquery

import logging
log = logging.getLogger(__name__)

class OutageMapWidget(LiveWidget, PolyMap):
    topic="map_geojson"

    onmessage ="addGeoJsonToPolymap('${id}', json, null)"

    interact = True
    hash = True
    cloudmade_api_key = "1a1b06b230af4efdbb989ea99e9841af"

    # To style the map tiles
    cloudmade_tileset = 'midnight-commander'

    resources = LiveWidget.resources + PolyMap.resources
