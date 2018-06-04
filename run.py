from flask import Flask
import os
from config import app_config


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(app_config[config_filename])

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    @app.errorhandler(403)
    def forbidden(error):
        return "Your are not authorized to view this page", 403

    @app.errorhandler(404)
    def page_not_found(error):
        return "The resource you are looking for is not available", 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return "The server encountered internal eror", 500

    return app

if __name__=="__main__":
    app = create_app("production")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)