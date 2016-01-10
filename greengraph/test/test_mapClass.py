from mock import patch
from mock import MagicMock
import requests
import numpy as np
import os
from nose.tools import assert_almost_equal
from greengraph.map import *

defaultLat = 51.5073509
defaultLong = -0.1277583

def setup_module(module):
    '''
    This function is the first one to be executed in this module. It creates a synthetic image with no green pixels and saves it in a csv file to be accessed as a fixture in the functions.
    '''
    print('Setup module')

    # create file with an image with no green pixels
    mapImgR=np.ones((300,300))
    mapImgG=np.zeros((300,300))
    mapImgB=np.ones((300,300))

    # savetxt only works with <2dim arrays
    np.savetxt("greengraph/fixtDataRed.csv", mapImgR, delimiter=",")
    np.savetxt("greengraph/fixtDataGreen.csv", mapImgG, delimiter=",")
    np.savetxt("greengraph/fixtDataBlue.csv", mapImgB, delimiter=",")


def teardown_module(module):
    '''
    This function is called after everything else in this module. Its purpose is to close any connections to the internet or a database. In this case, it deletes the .csv files created in the setup_module() function.
    '''
    print('Teardown module')
    ########################
    # # uncomment to delete the fixture data
    # os.remove('greengraph/fixtDataRed.csv')
    # os.remove('greengraph/fixtDataGreen.csv')
    # os.remove('greengraph/fixtDataBlue.csv')


def test_defaultRequestParam():
    '''
    Test function to check that the http get request is called with the right parameters in the default case.
    '''
    with patch.object(requests,'get') as mock_getRequest:
        print('mock requests was called')
        defaultMap= getMapAt(defaultLat,defaultLong)
        params=dict(
            sensor='false',
            zoom=10,
            size='400x400',
            center=",".join(map(str, (defaultLat,defaultLong) )),
            style='feature:all|element:labels|visibility:off'
            )
        params["maptype"]="satellite"

        mock_getRequest.assert_called_with(
        "http://maps.googleapis.com/maps/api/staticmap?",params=params)

def test_countGreen_nonGreenImg():
    '''
    Test to count the number of green pixels in a photo with no green areas. The image is read from the fixture .csv file created in the setup_module() function.
    '''
    myDataRed = np.genfromtxt('greengraph/fixtDataRed.csv', delimiter=',')
    myDataGreen = np.genfromtxt('greengraph/fixtDataGreen.csv', delimiter=',')
    myDataBlue = np.genfromtxt('greengraph/fixtDataBlue.csv', delimiter=',')
    mapImg=np.dstack((myDataRed, myDataGreen, myDataBlue))

    # create Map object with the test image
    testMap=Map(defaultLat,defaultLong)
    testMap.setDummyImage(mapImg)
    print(str(testMap.count_green()))
    assert_almost_equal (testMap.count_green(),0,delta=1e-5)


# @patch('greengraph.map.Map')
# def getMapMock(mockMap):
#     print('patch decorator')
#     myDataRed = np.genfromtxt('fixtDataRed.csv', delimiter=',')
#     myDataGreen = np.genfromtxt('fixtDataGreen.csv', delimiter=',')
#     myDataBlue = np.genfromtxt('fixtDataBlue.csv', delimiter=',')
#     mapImg=np.dstack((myDataRed, myDataGreen, myDataBlue))
#
#     mockMap.pixels=mapImg
#
#     numGreenPix=mockMap.count_green()
#     print('green pix = '+ str(numGreenPix))


# define fixture with a numpy array of 3 green pixels -> test count_green() test that it works with no green pixels and only green pixels

# test save_green with my fixture
