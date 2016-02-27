from flask import jsonify

from habanero import app, __version__


@app.route("/api/v1/")
def index():
    data = {
        'name': 'habanero',
        'version': __version__,
        'url': 'http://habanero.antojitos.io/',
    }
    return jsonify(**data)
