def aStarAlgo(start_node, stop_node):
    if start_node not in Graph_nodes or stop_node not in Graph_nodes:
        print("Start or stop node not found in the graph.")
        return None

    open_set = {start_node}
    closed = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        node = min(open_set, key=lambda x: closed[x] + heuristic(x))

        if node == stop_node:
            path = []
            while node != start_node:
                path.append(node)
                node = parents[node]
            path.append(start_node)
            return path[::-1]

        open_set.remove(node)

        for newnode, weight in get_neighbors(node) or []:
            tentative_g = closed.get(node, float('inf')) + weight
            if tentative_g < closed.get(newnode, float('inf')):
                closed[newnode] = tentative_g
                parents[newnode] = node
                open_set.add(newnode)


    print("No path found from start to stop node.")
    return None

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n)

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 2), ('G', 1)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G':None
}

print(aStarAlgo('A', 'G'))
