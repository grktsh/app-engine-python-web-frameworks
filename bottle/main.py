from bottle import Bottle

app = Bottle()


@app.route('/<name>')
def hello(name):
    return {'hello': name}
