#app.py

import settings

from flask import Flask, Blueprint
from flask_restplus import Swagger
from japaneseToRomaji

## Create the app
app = Flask(__name__)
app.register_blueprint(Blueprint('api', __name__))

## Register the resources
api.add_namespace(languages_namespace)

## Config the app
app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
app.config['SWAGGER_UI_ENABLED'] = settings.SWAGGER_UI_ENABLED

## Set up swagger
Swagger(app)
