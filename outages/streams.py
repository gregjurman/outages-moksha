from moksha.api.streams import PollingDataStream
import json

class OutageStatStream(PollingDataStream):
    frequency = 2.0

    counter = 0

    jsonify = True

    def poll(self):
        self.counter = self.counter + 1
        self.send_message('stat_outages', {
            'text' : str(self.counter)
        })
