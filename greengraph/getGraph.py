from graph import Greengraph
from matplotlib import pyplot as plt

def plotGreenDistribution(startPos, endPos, steps, outFile):
    # compute the proportion of green pixels
    myGraph=Greengraph(startPos,endPos)
    data=myGraph.green_between(steps)
    titleString='Proportion of green pixels between ' + startPos+ ' and ' + endPos
    plt.plot(data)
    plt.xlabel('Distance steps')
    plt.ylabel('Number of green pixels')
    plt.title(titleString)
    plt.savefig(outFile)
