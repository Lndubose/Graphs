#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    # print(graph.vertices)

    graph.bft('2')  # Returns ['2']
    print(graph.bft('0'))  # Returns ['0', '3', '1']

    print(graph.dft('0'))  # Returns ['0', '1', '3']

    print(graph.dft_r('0'))


if __name__ == '__main__':
    # TODO - parse argv
    main()
