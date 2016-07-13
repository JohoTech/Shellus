from flask import Flask, request, url_for, sessions
from flask_api import FlaskAPI, status, exceptions, decorators, renderers, parsers
from .shellus_app import *
import json
import jsonify

app = Flask("shellus")

@app.route("/client", method='GET')
def client_list():
    return "all clients", status.HTTP_200_CREATED

@app.route("/client", method='POST')
def client_insert():
    return note_repr(idx), status.HTTP_201_CREATED

app.run(debug=True)