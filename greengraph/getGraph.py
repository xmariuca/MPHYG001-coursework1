from graph import Greengraph
from matplotlib import pyplot as plt
'''
.. function:: plotGreenDistribution
'''

def plotGreenDistribution(startPos, endPos, steps, outFile):
    '''
    Generate a plot with the distribution of green pixels between two locations.

    Input:
    ------
    :param startPos: A starting location, like 'London'.
    startPos : str
        A starting location, like 'London'.
    endPos : str
        An ending location, like 'Cambdrige'.
    steps : int
        A number of steps to discretise the space between the two locations, like 15
    outFile : str
        A filename to be used for saving the plot, like 'outGraph.png'

    Output:
    -------
    A file with the graph representing the distribution of green pixels.

    '''
    # compute the proportion of green pixels
    myGraph=Greengraph(startPos,endPos)
    data=myGraph.green_between(steps)
    titleString='Proportion of green pixels between ' + startPos+ ' and ' + endPos
    plt.plot(data)
    plt.xlabel('Distance steps')
    plt.ylabel('Number of green pixels')
    plt.title(titleString)
    plt.savefig(outFile)
