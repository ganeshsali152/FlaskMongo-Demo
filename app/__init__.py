import os
from flask import Flask,jsonify,make_response
from flask_cors import CORS
from app import db
from flask_mongoengine import MongoEngine
mongo = db.init_db()

#----------created app functionality----------

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()
    CORS(app)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify(error='Not found'), 400)

    @app.errorhandler(500)
    def error_500(error):
        return make_response(jsonify(error='Internal Server Error'), 500)

    db.get_db(mongo=mongo, app=app)

    from app import api
    app.register_blueprint(api.bp)

    return app

cg_api_python = create_app()
