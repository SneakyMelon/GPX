
"""
    Formulas.py

    Some useful formulas that can be used and imported thru-out.
"""


from math import radians, sin, cos, atan2, sqrt
from GPSCoordinate import GPSCoordinate

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


def calories_burned(weight:float, speed: float, minutes:int=1):
    """ Calculate an estimate of calories burned during excercise.
        
        You'll need to know your weight, the activity, and duration of activity. 
        
        It uses the following formula to calculate how many calories per minute 
        you will burn during the activity and then multiply that number by your
        total exercise minutes.

            Energy expenditure (calories/minute) = .0175 x MET x weight (in kilograms)

        * https://www.hss.edu/conditions_burning-calories-with-exercise-calculating-estimated-energy-expenditure.asp

        @param weight   Persons weight in Kilograms
        @param speed    Speed a person is travelling
        @param minutes  Number of minutes spent excercising at this speed

        TODO needs verification to files and input values
    """

    import json

    with open('./resources/met-efforts.json') as f:
        j = json.load(f)

    weight = float(weight)
    speed = float(speed)
    minutes = int(minutes)

    EFFORT = [x for x in j['met']['running'] if x['speed']==speed][0]
    MET = EFFORT['met']
    kCal = 0

    kCal = (0.0175 * MET * weight) * minutes
    return kCal