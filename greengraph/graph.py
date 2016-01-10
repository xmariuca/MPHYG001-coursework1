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
        # When exactly_one is False, and there is at least one result, returns a list of geopy.location.Location objects
        # [0][0] - Address like London,UK
        # [0][1] - Long and latitude - for London = (51.5073509, -0.1277583)
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
        # for each geolocated place, a Map object is created -> which has the associated png image as an attribute -> we call count_green() on its pixels
        return [Map(*location).count_green()
                for location in self.location_sequence(
                    self.geolocate(self.start),
                    self.geolocate(self.end),
                    steps)]
