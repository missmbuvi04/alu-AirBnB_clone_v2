#!/usr/bin/python3
"""
Flask web application for AirBnB clone - HBNB filters
This module creates a Flask web application that displays HBNB filters.
The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
import os


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display HTML page with HBNB filters
    Load State, City and Amenity objects from DBStorage
    """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    print(f"Server is running on http://{host}:{port}/")
    print("Press CTRL+C to stop the server")
    app.run(host=host, port=port)
