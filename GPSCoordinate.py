
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

        return self._to_dms()

    def __repr__(self):
        return '<class {}({},{})>'.format(self.__class__.__name__, self.latitude, self.longitude)

    def _to_dms(self)->str:
        """Convert a GPS coordinate from a float into a degree-minute-second"""

        # Function requirements variables
        latitude = self.latitude
        longitude = self.longitude
  
        # Get directions on map
        _NS_direction = "N" if latitude >= 0 else "S"
        _EW_direction = "E" if longitude >= 0 else "W"


        dms_lat = self._get_dms(latitude)
        dms_long= self._get_dms(longitude)

        rtn = "{} {}°{}'{}\" {} {}°{}'{}\"".format( _NS_direction, dms_lat[0], dms_lat[1], dms_lat[2],
                                                    _EW_direction, dms_long[0], dms_long[1], dms_long[2])
        return rtn

    def _get_dms(self, position):
        """Convert latitude or longitude positions into degree-minute-seconds (DMS) style
        
            Degrees:
                To get the degrees, we split the whole number (gps position) 
                and leave the remainder. This becomes the degrees.

                56.34346 => 56
            Minutes:
                To get the minutes, we get the remainder of degrees and 
                multiply the remainder by 60, and use the whole number.
                If the number is negative, to get the same result, take away
                the remainder from 1 to get the same result as possitive numbers.

                0.34346 * 60 => 20.6076 ==> 20
            Seconds:
                Multiply the new remainder of Minutes by 60, and this gives the
                seconds. This can be rounded up or down, and rounded to as many
                places as wanted.
                
                0.6076 * 60 => 36.456
            
            DMS then becomes 56 degrees, 20 minutes, 36.456 seconds
        """
        
        # GPS position to be converted to DMS
        position = position 
        _d, _m, _s  = None, None, None
        _d = int(position)                          
        _m_remainder = (1 - (position % 1)) if position < 0 else position % 1
        _m = int(_m_remainder * 60)              
        _s_remainder = (_m_remainder * 60) % 1
        _s = round((_s_remainder * 60), 3)

        return (_d, _m, _s)

    def _verify(self):
        """Ensure that the values passed are within acceptable ranges"""
 
        # Check if int or float
        if not (isinstance(self.latitude, float) or isinstance(self.latitude, int)):
            raise TypeError("Unsupported GPS data type for latitude.")
        if not (isinstance(self.longitude, float) or isinstance(self.longitude, int)):
            raise TypeError("Unsupported GPS data type for longitude.")

        # Check if co-ordinates are within correct ranges
        # Verified if -180 <= lat <= 180 (between)
        if not self._latitude_range['min'] <= self.latitude <= self._latitude_range['max']: 
            raise ValueError("The GPS latitude value exceeds the min/max values set.")

        if not self._longitude_range['min'] <= self.longitude <= self._longitude_range['max']: 
            raise ValueError("The GPS longitude value exceeds the min/max values set.")
