import numpy as np
from StringIO import StringIO
from matplotlib import image as img
import requests

def getMapAt(lat, long, satellite=True, zoom=10, size=(400,400), sensor=False):
    base="http://maps.googleapis.com/maps/api/staticmap?"
    params=dict(
        sensor= str(sensor).lower(),
        zoom= zoom,
        size= "x".join(map(str, size)),
        center= ",".join(map(str, (lat, long) )),
        style="feature:all|element:labels|visibility:off"
      )
    if satellite:
        params["maptype"]="satellite"
    return requests.get(base, params=params)


class Map(object):
    '''
    The Map class handles the interaction with Google maps and counts the amount of green pixels in a given image.
    '''
    def __init__(self, lat, long, satellite=True, zoom=10, size=(400,400), sensor=False):
        self.response=getMapAt(lat, long, satellite=True, zoom=10, size=(400,400), sensor=False)
        # Fetch our PNG image data
        self.image=self.response.content
        # Parse our PNG image as a numpy array
        self.pixels = img.imread(StringIO(self.image))

    def setDummyImage(self, testImg):
        self.pixels= None
        self.pixels = testImg

    def green(self, threshold):
        '''
        .. method:: Use NumPy to build an element-by-element logical array
        '''
        # Use NumPy to build an element-by-element logical array
        greener_than_red = self.pixels[:,:,1] > threshold* self.pixels[:,:,0]
        greener_than_blue = self.pixels[:,:,1] > threshold*self.pixels[:,:,2]
        green = np.logical_and(greener_than_red, greener_than_blue)
        return green

    def count_green(self, threshold = 1.1):
        '''
        .. method:: Count the number of green pixels in the current map
        '''
        return np.sum(self.green(threshold))

    def show_green(data, threshold = 1.1):
        '''
        .. method:: Save the green pixels of the current map
        '''
        green = self.green(threshold)
        out = green[:,:,np.newaxis]*array([0,1,0])[np.newaxis,np.newaxis,:]
        buffer = StringIO()
        result = img.imsave(buffer, out, format='png')
        return buffer.getvalue()
