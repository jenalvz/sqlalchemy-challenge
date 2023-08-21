# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)
Base.classes.keys

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes"""
    return(
        f"All available routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

### Precipitation route
@app.route("/api/v1.0/precipitation")

def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation data"""
    
    # Query alll precipitation data
    results = session.query(measurement.date, measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precip
    all_precip = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict['Date'] = date
        all_precip.append(precipitation_dict)

    return jsonify(all_precip)



### Stations route
@app.route("/api/v1.0/stations")

def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all station data"""
    
    # Query alll station data
    results = session.query(station.station, station.name, station.latitude, station.longitude, station.elevation).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station, name, latitude, longitude, elevation in results:
        station_dict = {}
        station_dict['station'] = station
        station_dict['name'] = name
        station_dict['latitude'] = latitude
        station_dict['longitude'] = longitude
        station_dict['elevation'] = elevation
        all_stations.append(station_dict)

    return jsonify(all_stations)


# ### TOBS route
# @app.route("/api/v1.0/tobs")

# def tobs():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all TOBS data fir station USC00519281"""
    
#     # Query alll station data
#     results = session.query(station.station, station.name, station.latitude, station.longitude, station.elevation).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_stations


### note to grader:  will submit for feedback and meet with a TA/tutor to troubleshoot. will make use of multiple submission attempts.
