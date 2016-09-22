"""
4.2
Given a directed graph, design an algorithm to find out whether there is a route between
two nodes
"""
# Refer to: https://www.python.org/doc/essays/graphs/

# uses backtracking: it tries each possibility in turn until it finds a solution.
# the list path represents
def find_path(graph, start, end, path=[]):
    if not graph.has_key(start):
        return None

    path = path + [start] # list + list creates a new list

    if start == end: # end to recursion; we found the end node
        return path

    for node in graph[start]:
        if node not in path: # Check that we have not visited this node already
            newPath = find_path(graph, node, end, path)
            if newPath:
                return newPath
    return None

def find_all_paths(graph, start, end, path=[]):
    if not graph.has_key(start):
        return []

    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

if __name__ == '__main__':

    # Key = Node, Value = List of nodes that have a direct arc from key node
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['E'],
             'E': ['F'],
             'F': ['C']}
    print find_path(graph, 'A', 'C')
    print find_all_paths(graph, 'A', 'C')