import numpy as np
import geopy
from map import Map

class Greengraph(object):
    '''
    Main public class that does something.

    '''
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

    def geolocate(self, place):
        '''
        .. method:: Locates the given position on the map
        '''
        return self.geocoder.geocode(place, exactly_one=False)[0][1]

    def location_sequence(self, start,end,steps):
        '''
        .. method:: Discretize the space between the start and end point
        '''
        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):
        '''
        .. method:: Counts the green pixels between the two locations
        '''
        return [Map(*location).count_green()
                for location in self.location_sequence(
                    self.geolocate(self.start),
                    self.geolocate(self.end),
                    steps)]
