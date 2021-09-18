#!/usr/bin/python3
"""
api module
"""
from flask import Flask, make_response, render_template, url_for
from models import storage
from api.v1.views import app_views
import os

# flask application variable: app
app = Flask(__name__)

# flask server environmental setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# registers app_views BluePrint
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """
    calls close method on currebt sqlAlchemy session
    """
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 errors
    """
    code = exception.__str__().split()[0]
    desc = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)

if __name__ == "__main__":
"""
initializes Flask app
"""
app.run(host=host, port=port)
