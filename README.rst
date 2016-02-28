========
Habanero
========

The hottest authentication pepper available.

This project is a very simple authentication backend to be used with
the NGINX's ``auth_request`` directive.
See http://nginx.org/en/docs/http/ngx_http_auth_request_module.html for
more details.


Running the server
------------------

Run the Habanero server::

    python src/runserver.py

Now, you can point your browser to http://localhost:5000/

In order to use your own settings, you can make a copy of the defaults
settings and used it exporting ``HABANERO_SETTINGS``::

    cp src/habanero/default_settings.py settings.py
    vim settings.py
    HABANERO_SETTINGS=../../settings.py src/runserver.py


Usage
-----

You can interact with the Habanero server using ``curl``::

    $ curl -i -H "X-API-KEY: DqX03pg2dJfBma" -H "X-API-SECRET: aaa7bf61cb722c1680165f991db3f0371de438f6" 127.0.0.1:5000/api/v1/auth
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 57
    Server: Werkzeug/0.11.4 Python/2.7.6
    Date: Sun, 28 Feb 2016 00:55:44 GMT
    
    {
      "message": "User myuser authenticated for App1."
    }

