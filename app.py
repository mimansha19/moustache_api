"""
Moustache Escapes - Nearby Property Recommendation API

This Flask-based application helps tele-calling agents identify Moustache Escapes
properties within a 50km radius of a location specified by a customer (even with 
minor typos in the query). It supports real-time search using fuzzy matching and
distance calculations based on geographic coordinates.

Author: Mimansha Agarwal IIT BHU Varanasi
Date: 6th April 2025
"""

from flask import Flask, request, jsonify
from utils import correct_spelling, geocode_location, haversine
from properties import properties

app = Flask(__name__)

@app.route('/nearby-properties', methods=['POST'])
def get_nearby_properties():
    '''
        - API Endpoint: /nearby-properties
        - Method: POST
        - Input: JSON { "query": "<location_name>" }

        Returns:
            - 200 OK with list of properties and distances
            - 400 Bad Request if input is invalid or location cannot be geocoded
    '''
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"result": "Missing query"}), 400

    corrected_query = correct_spelling(query)
    if not corrected_query:
        return jsonify({"result": "Could not find the location"}), 400

    lat, lon = geocode_location(corrected_query)
    if lat is None or lon is None:
        return jsonify({"result": "Could not find the location"}), 400

    nearby = []
    for prop in properties:
        dist = haversine(lat, lon, prop["latitude"], prop["longitude"])
        if dist <= 50:
            nearby.append({
                "name": prop["name"],
                "distance_km": round(dist, 2)
            })

    if not nearby:
        return jsonify({"result": "No properties found within 50km of the given location."})

    return jsonify({"result": nearby})

PORT=5000
app.run(port=PORT)