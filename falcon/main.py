import falcon
from falcon.util import json


class Hello(object):
    def on_get(self, req, resp, name):
        resp.body = json.dumps({'hello': name})


app = falcon.API()
app.add_route('/{name}', Hello())
