# coding: utf-8
from mock import MagicMock
from greengraph.graph import Greengraph
from nose.tools import assert_almost_equal


def test_geolocate():
	'''
	Test the geolocate function in the Greengraph() class. A MagicMock object is created for the geocoder.
	'''
	myGreengraph = Greengraph("London","Cambdrige")
	# defaultResp = ["London",(51.5073509, -0.1277583)]

	tGeocoder = MagicMock()
	# tGeocoder = mock.Mock()
	# attrs = {'geocode.return_value': defaultResp, 'other.side_effect': KeyError}
	# tGeocoder.configure_mock(**attrs)

	defaultResp = []
	defaultResp.append([])
	defaultResp[0].append("London")
	defaultResp[0].append((51.5073509, -0.1277583))

	tGeocoder.geocode.return_value = defaultResp
	myGreengraph.geocoder = tGeocoder

	tGeocoder.geocode.assert_not_called()

	startLocation = myGreengraph.geolocate(myGreengraph.start)
	# print(startLocation)
	# testLoc = tGeocoder.geocode("London", exactly_one=False)
	# print(testLoc)
	# print(tGeocoder.method_calls)

	assert_almost_equal(startLocation,(51.5073509, -0.1277583))

	tGeocoder.geocode.assert_called_with("London", exactly_one=False)
