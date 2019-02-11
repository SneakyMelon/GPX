
"""
    GPSCoordinate.py

    Creates a GPS supported co-ordinate based class.

    ? Feels like it should be seperate classes for GPS and Co-ordinates
    ?   --> GPS inherits properties of co-ordinates
"""

class GPSCoordinate:
    """ Creates a Point-style co-ordinate class"""
    
    # The valid range of latitude in degrees is -90 and +90 
    # for the southern and northern hemisphere respectively.
    _latitude_range  = {'min': -90, 'max': 90}

    # Longitude is in the range -180 and +180 specifying 
    # coordinates west and east of the Prime Meridian.
    _longitude_range = {'min':-180, 'max':180}
    
    def __init__(self, latitude:float, longitude:float):
       
        # Create class attributes
        self.latitude   = latitude
        self.longitude  = longitude

        # Verify the co-ordinates. Class assignment should fail if it can not
        # get passed this method.
        self._verify()
       
    def __str__(self):
        return "{}|{}".format(self.latitude, self.longitude)

    def __repr__(self):
        return '<class {}({},{})>'.format(self.__class__.__name__, self.latitude, self.longitude)

    def _verify(self):
        """Ensure that the values passed are within acceptable ranges"""
 
        # Check if int or float
        if not isinstance(self.latitude, float) or not isinstance(self.latitude, int):
            raise TypeError("Unsupported GPS data type.")
        if not isinstance(self.longitude, float) or not isinstance(self.longitude, int):
            raise TypeError("Unsupported GPS data type.")

        # Check if co-ordinates are within correct ranges
        # Verified if -180 <= lat <= 180 (between)
        if not self._latitude_range['min'] <= self.latitude <= self._latitude_range['max']: 
            raise ValueError("The GPS latitude value exceeds the min/max values set.")

        if not self._longitude_range['min'] <= self.longitude <= self._longitude_range['max']: 
            raise ValueError("The GPS longitude value exceeds the min/max values set.")
