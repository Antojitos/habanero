from flask import Flask

__version__ = '0.0.1'

app = Flask(__name__)
app.config.from_object('habanero.default_settings')
app.config.from_envvar('HABANERO_SETTINGS', silent=True)

import habanero.views
