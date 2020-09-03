from flask import Flask
from config import host


def create_app(config_filename):
    app = Flask(__name__)   # initialize flask application
    app.config.from_object(config_filename)

    from app import api

    @app.after_request
    def after_request(response):
        """Add the headers in response after a requests"""
        response.headers.add('Access-Control-Allow-Origin',
                            ':'.join(("http://"+host+"",
                                    str("4200"))))
        response.headers.add('Access-Control-Allow-Headers',
                            'origin, content-type, accept')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    api.init_app(app)

    return app

app = create_app("config")


if (__name__ == "__main__"):

    app = create_app("config")
    #app.run(debug = True, port = 8765,ssl_context=('cert.pem', 'key.pem'))
    app.run(debug = True, port = 8765)