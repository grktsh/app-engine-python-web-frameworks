from pyramid.config import Configurator


def hello_world(request):
    return {'hello': request.matchdict['name']}


with Configurator() as config:
    config.add_route('hello', '/{name}')
    config.add_view(hello_world, route_name='hello', renderer='json')
    app = config.make_wsgi_app()
