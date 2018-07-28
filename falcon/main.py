import falcon


class Hello(object):
    def on_get(self, req, resp, name):
        resp.media = {'hello': name}


app = falcon.API()
app.add_route('/{name}', Hello())
