#!/usr/bin/python3
"""
Returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status', methods=['GET'])
def status():
    """
    json method that returns state of status
    """
    if request.method = 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    returns a count of all objects
    """
    if request.method == 'GET':
        response = {}
        counts = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in counts.items():
            counts[value] = storage.count(key)
        return jsonify(counts)
