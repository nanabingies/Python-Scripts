# All this is theoretical of course.
# This is a collection of scripts i found online while learning about graph theory
# Mostly https://python-course.eu/applications-python/graphs-python.php

'''
        a       b
         \     /|
          \   / |
            c   |      f
           / \  |
          /   \ |
        d       e
'''

# graphs in python are represented as sets
graph = {
    'a': {'c'},
    'b': {'c', 'e'},
    'c': {'a', 'b', 'd', 'e'},
    'd': {'c', 'e'},
    'e': {'b', 'c'},
    'f': {}
}

print(graph)