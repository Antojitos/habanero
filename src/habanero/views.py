from flask import jsonify, request

from habanero import app, __version__


@app.route("/api/v1/")
def index():
    data = {
        'name': 'habanero',
        'version': __version__,
        'url': 'http://habanero.antojitos.io/',
    }
    return jsonify(**data)


@app.route("/api/v1/auth", methods=['GET'])
def auth():
    api_keys = app.config['API_KEYS']
    key = request.headers.get('x-api-key')
    secret = request.headers.get('x-api-secret')

    if key in api_keys:
        username, secrets = api_keys[key]
        if secret in secrets:
            app_name = secrets[secret]
            message = 'User %s authenticated for %s.' % (username, app_name)
            return jsonify({'message': message}), 200

    message = 'Authentication credentials were missing or incorrect.'
    return jsonify({'message': message}), 401
