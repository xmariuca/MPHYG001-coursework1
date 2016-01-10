from nose.tools import assert_raises
from greengraph.getGraph import plotGreenDistribution


def test_negativeSteps():
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'Cambridge', -5, 'out.png')

def test_wrongTypeSteps():
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'Cambridge', '5', 'out.png')

def test_emptyStartingPosition():
    with assert_raises(ValueError):
        assert plotGreenDistribution('', 'Cambridge', 9, 'out.png')

def test_emptyEndingPosition():
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', '', 9, 'out.png')

def test_emptyOutputFilename():
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'Cambridge', 9, '')

def test_emptyStartingPosition():
    with assert_raises(ValueError):
        assert plotGreenDistribution('', 'Cambridge', 9, 'out.png')

def test_identicalStartingAndEndingPositions():
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'London', 9, 'out.png')
