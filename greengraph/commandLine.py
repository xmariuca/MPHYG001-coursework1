#!/usr/bin/env python
from argparse import ArgumentParser
from graph import Greengraph
from matplotlib import pyplot as plt
from map import Map

def parseArgs():
    prs= ArgumentParser(description="Greengraph package - Generates a graph with the proportion of green pixels between two locations")
    prs.add_argument('--from',help='Start position, default = London', dest='startPos', default='London')
    prs.add_argument('--to',help='End position, default = Cambridge', dest='endPos', default='Cambridge')
    prs.add_argument('--steps',help='Number of steps between start and end, default = 10', default=10, type=int)
    prs.add_argument('--out',help='Name of output image, default = outGraph.png', default='outGraph.png')
    arguments=prs.parse_args()

    # compute the proportion of green pixels
    myGraph=Greengraph(arguments.startPos,arguments.endPos)
    data=myGraph.green_between(arguments.steps)
    titleString='Proportion of green pixels between ' + arguments.startPos+ ' and ' + arguments.endPos
    plt.plot(data)
    plt.xlabel('Distance steps')
    plt.ylabel('Number of green pixels')
    plt.title(titleString)
    plt.savefig(arguments.out)


if __name__=='__main__':
    parseArgs()
