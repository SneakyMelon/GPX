
"""
    GPSCoordinate.py

    Co-ordinate class similaiar to Point where a GPS coordinate
    can be accessed such as gps.latitude and gps.longitude
"""

class GPSCoordinate:
    """ Creates a Point-style co-ordinate class """

    def __init__(self, latitude:float=None, longitude:float=None):
        """
            ! Needs to add latitude and longitude integer and float check
            ! so that we do not try and set them to something like a string.

        """
        if latitude==None or longitude==None:
            raise ValueError("Latitude and Longitude can not be empty.")

        self.latitude   = latitude
        self.longitude  = longitude

        self._verify()

        
    def __str__(self):
        return "{}|{}".format(self.latitude, self.longitude)

    def __repr__(self):
        return '<class {}({},{})>'.format(self.__class__.__name__, self.latitude, self.longitude)

    def _verify(self):
        """
            Verify that the values passed to this class are proper.
            
            ? Needs implemented
        """


