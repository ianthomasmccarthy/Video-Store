from flask import flash, redirect, abort, url_for, request, json
from app import app


@app.before_request
def before_request():
    pass


@app.errorhandler(404)
def not_found_error(error):
    return "404 Not Found Error"


@app.errorhandler(500)
def internal_server_error():
    return "500 internal Server Error"


@app.route('/')
@app.route('/index')
def index():
    return "Hello World"
