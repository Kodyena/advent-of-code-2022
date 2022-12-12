import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def draw_plot(arr):
    fig = plt.figure(figsize=(10,10))
    height = max([node.get_coords()[0] for node in arr]) + 1
    width = max([node.get_coords()[1] for node in arr]) + 1
    map = np.full([height, width], -1)
    for node in arr:
        map[node.get_coords()[0]][node.get_coords()[1]] = node.get_value()
    masked_array = np.ma.masked_where(map == -1, map)
    cmap = matplotlib.cm.plasma
    cmap.set_bad(color='white')
    plt.imshow(masked_array, cmap=cmap)
    plt.show()

class Node:
        __connected_nodes: set['Node']
        __coords: list[int]
        __value: int 
        
        def __init__(self, coords, value, connected_nodes = None) -> None:
            self.__coords = coords
            self.__value = value
            if(connected_nodes is None):
                self.__connected_nodes = set()
            else:
                self.__connected_nodes = set(connected_nodes)
        def __repr__(self):
            return "coords: {}, value: {}".format(self.__coords, self.__value)
        def __str__(self) -> str:
            return self.__repr__()
        def add_connected_node(self, node):
            self.__connected_nodes.add(node)
        def get_coords(self): return self.__coords
        def get_value(self): return self.__value
        def get_connected_nodes(self): return self.__connected_nodes
        def get_all_connected_nodes(self, node = None, connectedNodes = None):
            if connectedNodes is None:
                connected_nodes = set()
            else:
                connected_nodes = connectedNodes
            if node is None:
                currentNode = self
            else:
                currentNode = node
            
            connected_nodes.add(currentNode)

            for node in currentNode.get_connected_nodes():
                if(node not in connected_nodes): connected_nodes.update(self.get_all_connected_nodes(node, connected_nodes))

            return connected_nodes

class NodeGraph:
    __nodes: set[Node]

    def __init__(self):
        self.__nodes = set()
    def add_node(self, node):
        self.__nodes.add(node)
    def get_nodes(self):
        return self.__nodes
    def get_node(self, coord):
        return next(filter(lambda node: node.get_coords()[0] == coord[0] and node.get_coords()[1] == coord[1], self.__nodes), None)
    def find_shortest_path(self, start_point, end_point):
        start_node = self.get_node(start_point)
        end_node = self.get_node(end_point)
        traversals = dict()
        traversals[start_node] = None
        frontier = []
        reached_nodes = set()
        frontier.insert(0, start_node)
        reached_nodes.add(start_node)

        while not len(frontier) == 0:
            current_node = frontier.pop()
            for adj_node in current_node.get_connected_nodes():
                if adj_node not in reached_nodes:
                    frontier.insert(0, adj_node)
                    reached_nodes.add(adj_node)
                    traversals[adj_node] = current_node
        
        #draw_plot(reached_nodes)

        current_node = end_node
        path = []
        while current_node != start_node:
            path.append(current_node)
            try:
                current_node = traversals[current_node]
            except:
                return False
        path.append(start_node)
        path.reverse()
        return path

node_graph = NodeGraph()
height_map = np.array([[c for c in line] for line in open("Day12\Data.txt").read().split("\n")])

start_point = list(zip(*np.where(height_map == 'S')))[0]
end_point = list(zip(*np.where(height_map == 'E')))[0]

height_map[start_point[0], start_point[1]] = 'a'
height_map[end_point[0], end_point[1]] = 'z'

for i in range(len(height_map)):
    for j in range(len(height_map[1])):
        node_graph.add_node(Node([i, j], ord(height_map[i, j]) - ord('a')))

for node in node_graph.get_nodes():
    coords = node.get_coords()
    for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        adj_node = node_graph.get_node([coords[0] + i, coords[1] + j])
        if(adj_node is not None and adj_node.get_value() - node.get_value() <= 1):
            node.add_connected_node(adj_node)

###Q1###
shortest_path = node_graph.find_shortest_path(start_point, end_point)
print("Answer to Q1: {}".format(len(shortest_path) - 1))
#draw_plot(shortest_path)

###Q2###
a_nodes = [node for node in node_graph.get_nodes() if node.get_value() == 0]
shortest_paths = [node_graph.find_shortest_path(node.get_coords(), end_point) for node in a_nodes]
shortest_paths = list(filter(lambda p: p != False, shortest_paths))
shortest_path = min(shortest_paths, key=lambda p: len(p))
print("Answer to Q2: {}".format(len(shortest_path) - 1))
#draw_plot(shortest_path)