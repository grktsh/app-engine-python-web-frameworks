import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self, name):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.json = {'hello': name}


app = webapp2.WSGIApplication([
    webapp2.Route(r'/<name>', handler=MainHandler),
])
