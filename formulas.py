
"""
    Formulas.py

    Some useful formulas that can be used and imported thru-out.
"""


from math import radians, sin, cos, atan2, sqrt
from .GPSCoordinate import GPSCoordinate

def Haversine(coordinate1: GPSCoordinate=None, coordinate2:GPSCoordinate=None, output="miles|kilometers"):
    """Calculate the distance between two points on Earth"""
    
    if not isinstance(coordinate1, GPSCoordinate) or not isinstance(coordinate2, GPSCoordinate):
        raise ValueError("Co-ordinates must not be empty, and be of type 'GPSCoordinate' type.")

    # Earth Constants
    EarthRadius_M = 3959.87433 # Miles
    # EarthRadius_km = 6372.79999 # Kilometers
 
    # Initialise variables from paramaters
    lat1, long1 = coordinate1.latitude, coordinate1.longitude
    lat2, long2 = coordinate2.latitude, coordinate2.longitude
    
    # convert decimal degrees into radians
    rlat1, rlong1, rlat2, rlong2 = map(radians, [lat1, long1, lat2, long2])

    # Calculate the difference between the latitudes and longitudes
    dlon = rlong1 - rlong2
    dlat = rlat1 - rlat2  
    
    # Trigomatry stuff - It works so why question it???
    a = pow(sin(dlat/2), 2) + cos(rlat1) * cos(rlat2) * pow(sin(dlon/2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    # Calculate the distance
    distance =  c * EarthRadius_M
    return "{0:f} Miles".format(distance)