
"""
    Formulas.py

    Some useful formulas that can be used and imported thru-out.
"""

import json

from math import radians, sin, cos, atan2, sqrt
from GPSCoordinate import GPSCoordinate


def Haversine(coordinate1: GPSCoordinate, coordinate2:GPSCoordinate, output="miles|kilometers|M|km"):
    """
        Calculate the distance between two points on Earth
    
        TODO Create an output for function
    """
    
    if not isinstance(coordinate1, GPSCoordinate) or not isinstance(coordinate2, GPSCoordinate):
        raise ValueError("Co-ordinates must not be empty, and be of type 'GPSCoordinate' type.")

    if not (isinstance(output, str) and (output.lower() in ['miles', 'kilometers', 'km', 'M'])):
        raise ValueError('Output filter must be of type String, and be a supported type of measurement.')

    # Earth Constants
    EarthRadius_M = 3959.87433 # Miles (range from 3950-->3963)
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


def calories_burned(weight:float, speed:float, minutes:int=1, options:dict=dict()):
    """ Calculate an estimate of calories burned during excercise.
        
        In order to calculate an estimated amount of calories burned, you
        need to know the persons weight, the activity (and effort), as well
        as the duration of activity.
        
        The following formula is used to calculate how many calories you will
        burn for each same effort minute of the activity. 

        Energy expenditure (calories/minute) = .0175 x MET x weight (in kg)

        Source:
        * https://www.hss.edu/conditions_burning-calories-with-exercise-calculating-estimated-energy-expenditure.asp

        @param weight   Persons weight in Kilograms
        @param speed    Speed a person is travelling in miles per hour
        @param minutes  Number of minutes spent excercising at this speed
        @param options  Determines the input and output format of this function

        TODO The speed uses hardcoded values. Need to find 
        TODO  between two values to get the best fitting MET value.
    """

    if not (isinstance(weight, float) or isinstance(weight, int)):
        raise TypeError("Weight has to be of type 'int' or of type 'float', not", type(weight))
    
    if not (isinstance(speed, float) or  isinstance(speed, int)):
        raise TypeError("Speed has to be of type 'int' or of type 'float', not", type(speed))

    if not (isinstance(minutes, int)):
        raise TypeError("Minutes has to be of type 'int', not", type(minutes))

    if not (isinstance(options, dict)):
        raise TypeError("Options has to be of type 'dict', not", type(options))

    # Assign paramaters to local variables
    weight = weight
    speed = speed
    minutes = minutes
    options = options
    
    # Locals
    energy = 0

    # Default options
    options['weight'] = options['weight'] or 'kg'
    options['speed']  = options['speed'] or 'mph'
    options['calories'] = options['calories'] or 'kcal'

    # Currently supported options
    supported_formats = {
        'weight'  : ('kg','lbs'),
        'speed'   : ('mph','kph'),
        'calories': ('kcal','kj'),
    }

    # Check each option paramater to make ensure it is supported
    # Throws ValueError if value is not supported. Then checks
    # each value to make sure format is supported.
    for option in options:
        # for [weight, speed, calories] in [weight, speed, calories]

        if not option in supported_formats:
            raise ValueError('Unsupported option:', option)
        
        for suboption in supported_formats:
            if suboption in supported_formats:
                options[suboption] = options[suboption]
            else:
                raise ValueError("Unsupported suboption:", suboption)

    # Convert speed to mph from kph
    if options['speed'] == 'kph':
        speed = speed / 1.609

    # Convert from stone to lbs. Doing it in this order means
    # next if statement will catch the unit in lbs.

    # if options['weight'] == 'stone':
    #    lbs = (weight * 14) + (weight % 14)
    # options['weight'] = 'lbs'

    # Convert weight from pounds to kilograms
    if options['weight'] == 'lbs':
        weight = weight / 2.2

    with open('./resources/met-efforts.json') as f:   
        j = json.load(f)
    
    # EFFORT is a JSON object - get the first object that matches
    # the speed. Can access MET, SPEED and DESCRIPTION.
    EFFORT = [x for x in j['met']['running'] if x['speed']==speed][0]
    
    # Access MET for formula
    MET = EFFORT['met']
 
    # Calories burned
    energy = (0.0175 * MET * weight) * minutes

    # Convert energy expenditure to kj
    if options['calories'] == 'kj':
        energy = energy * 4.184

    return round(energy)
