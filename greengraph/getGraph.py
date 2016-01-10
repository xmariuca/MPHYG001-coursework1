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

    # make sure the input parameters are valid
    if not isinstance(steps,int):
        raise ValueError("The steps value: "+ str(steps)+" is not an integer")
    if not isinstance(startPos,str):
        raise ValueError("The start position: "+ str(startPos)+" is not a string")
    if not isinstance(endPos,str):
        raise ValueError("The end position: "+ str(endPos)+" is not a string")
    if not isinstance(outFile,str):
        raise ValueError("The output filename: "+ str(outFile)+" is not a string")

    if steps<=0:
        raise ValueError("The steps value: "+ str(steps)+" is non-positive")

    if len(startPos)==0:
        raise ValueError("The starting position: "+ startPos+" is empty")
    if len(endPos)==0:
        raise ValueError("The ending position: "+ endPos+" is empty")
    if len(outFile)==0:
        raise ValueError("The output filename: "+ outFile+" is empty")

    if startPos == endPos:
        raise ValueError("The start and the end position are the same!")

    myGraph=Greengraph(startPos,endPos)
    data=myGraph.green_between(steps)
    titleString='Proportion of green pixels between ' + startPos+ ' and ' + endPos
    plt.plot(data)
    plt.xlabel('Distance steps')
    plt.ylabel('Number of green pixels')
    plt.title(titleString)
    plt.savefig(outFile)
