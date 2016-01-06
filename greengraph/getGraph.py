from graph import Greengraph
from matplotlib import pyplot as plt

def plotGreenDistribution(startPos, endPos, steps, outFile):
    '''
    Generate a plot with the distribution of green pixels between two locations.

    :param startPos: A starting location, like 'London'
    :type startPos: string
    :param endPos: An ending location, like 'Cambdrige'
    :type endPos: string
    :param steps: A number of steps to discretise the space between the two locations, like 15
    :type steps: int
    :param outFile: A filename to be used for saving the plot, like 'outGraph.png'
    :type outFile: string

    :returns: A file with the graph representing the distribution of green pixels.

    '''
    myGraph=Greengraph(startPos,endPos)
    data=myGraph.green_between(steps)
    titleString='Proportion of green pixels between ' + startPos+ ' and ' + endPos
    plt.plot(data)
    plt.xlabel('Distance steps')
    plt.ylabel('Number of green pixels')
    plt.title(titleString)
    plt.savefig(outFile)
