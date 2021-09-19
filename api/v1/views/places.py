#!/usr/bin/python3
"""
places views module
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC
from os import environ
STORAGE_TYPE = environ.get('HBNB_TYPE_STORAGE')


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'])
def places_per_city(city_id=None):
    """
    handles http method for requested places by city
    """
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        all_places = storage.all('Place')
        city_places = [obj.to_json() for obj in all_places.values()
                       if obj.city_id == city_id]
        return jsonify(city_places)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        user_id = req_json.get("user_id")
        if user_id is None:
            abort(400, 'Missing user_id')
        user_obj = storage.get('User', user_id)
        if user_obj is None:
            abort(404, 'Not found')
        if req_json.get("name") is None:
            abort(400, 'Missing name')
        Place = CNC.get("Place")
        req_json['city_id'] = city_id
        new_object = Place(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201

@app_views.route('/places/<place_id>', methods=['GET', 'DELETE', 'PUT'])
def places_with_id(place_id=None):
    """
    handles http methods for a given place using place_id
    """
    place_obj = storage.get('Place', place_id)
    if place_obj is None:
        abort(404, 'Not found')@
