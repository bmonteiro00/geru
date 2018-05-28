import urllib
import json


class Connection:
    """ This class is used to consume
        the REST API"""

    def __init__(self):
        self.server = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'
        self._data = json.dumps({"json": "obj"}, sort_keys=True, indent=4, separators=(',', ': '))
        self._get_all_quotes()

    def _get_all_quotes(self):
        req = urllib.request.Request(self.server)
        with urllib.request.urlopen(req) as response:
            self._data = json.loads(response.read().decode('utf-8'))

    def get_response(self):
        return self._data
