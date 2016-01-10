from nose.tools import assert_raises
from greengraph.getGraph import plotGreenDistribution


def test_negativeSteps():
    '''
    Test whether the steps variable is always positive
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'Cambridge', -5, 'out.png')

def test_wrongTypeSteps():
    '''
    Test whether the steps variable is an integer
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'Cambridge', '5', 'out.png')

def test_wrongTypeStartPos():
    '''
    Test whether the starting position is a string
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution((51.23,-1.2), 'Cambridge', 5, 'out.png')
def test_wrongTypeEndPos():
    '''
    Test whether the ending position is a string
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('Cambridge',(51.23,-1.2), 5, 'out.png')
def test_wrongTypeOutFile():
    '''
    Test whether the output filename is a string
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('London','Cambridge', 5, 555)

def test_emptyStartingPosition():
    '''
    Test whether the starting position is an empty string
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('', 'Cambridge', 9, 'out.png')

def test_emptyEndingPosition():
    '''
    Test whether the ending position is an empty string
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', '', 9, 'out.png')

def test_emptyOutputFilename():
    '''
    Test whether the filename of the output graph is an empty string
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'Cambridge', 9, '')

def test_identicalStartingAndEndingPositions():
    '''
    Test whether the starting and ending positions are identical
    '''
    with assert_raises(ValueError):
        assert plotGreenDistribution('London', 'London', 9, 'out.png')
