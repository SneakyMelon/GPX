
"""
    GPXDistances.py

    Manipulates the date from within a GPX File.
"""
# System level Imports
import xml.etree.ElementTree as ET

from datetime import datetime, timedelta
from shutil import copy2
from os import path

# Custom level Imports
from GPSCoordinate import GPSCoordinate
from backup import backup


trim_start  = 5 * 60
trim_end    = 5 * 60

d = datetime.strptime("1:20", "%H:%M")


file = "GPX File.gpx"

base = ET.parse(file)
root = base.getroot()

def get_element_text(xml_tree_obj:ET, element:ET.Element, namespace:str=""):
    """Find the first element that matches the element paramater"""
    
    root, element, ns = xml_tree_obj, element, namespace
    xpath = ".//{}{}".format(ns, element)

    return root.find(xpath).text


def get_trkpts():
    """trk represents a track - an ordered list of points describing a path. """

    # * Each point appears to vary between 2 and 3 seconds per update.
    # * This means there will be a new updated set of GPS at maximum
    # *   every 3 seconds, and a minimum of 2.

    if file == None:
        raise FileNotFoundError("No File arguement passed.")

    pts = [] #GPS points
    
    # Start counting time from zero
    total_time = timedelta(seconds=0)

    """
        ? Adding to time:

        ? Start time at zero        --> total_time = timedelta(seconds=0)
        ? Add some time to total    --> time_total.seconds + int(some_value)
        ?                           --> >> 100

        

    """

    for trkpts in root.iter(r'{http://www.topografix.com/GPX/1/1}trkpt'):
        #print(trkpt.attrib['lat'], trkpt.attrib['lon'])
    
        pts.append(trkpts.attrib)
    
    return pts





gps_marker_start = GPSCoordinate(56.4589780, -2.9626100)
gps_marker_end   = GPSCoordinate(56.4589420, -2.9625130)

"""
try:
    from backup import simple_backup
    simple_backup(filename)

except FileNotFoundError: # 
    pass
except ValueError: # filenames, destinations
    pass
except (OSError, IOError): #copy2
    pass
except Exception: # anything else uncaught / unknown error
    pass
"""