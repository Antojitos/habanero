from flask import jsonify, request, make_response

from habanero import app, __version__


@app.route("/api/v1/")
def index():
    data = {
        'name': 'habanero',
        'version': __version__,
        'url': 'https://github.com/Antojitos/habanero',
    }
    return jsonify(**data)


@app.route("/api/v1/auth", methods=['GET'])
def auth():
    api_keys = app.config['API_KEYS']
    key = request.headers.get('X-Api-Key')
    secret = request.headers.get('X-Api-Secret')

    if key in api_keys:
        username, secrets = api_keys[key]
        if secret in secrets:
            app_name = secrets[secret]
            message = 'User %s authenticated for %s.' % (username, app_name)
            response = make_response(jsonify({'message': message}), 200)
            response.headers.extend({'X-Auth-App': app_name})
            response.headers.extend({'X-Auth-Username': username})
            return response

    message = 'Authentication credentials were missing or incorrect.'
    return jsonify({'message': message}), 401
