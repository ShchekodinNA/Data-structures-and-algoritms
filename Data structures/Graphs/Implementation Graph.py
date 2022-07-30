# using adjacency list with hash table base

class Graph:  # undirected graph
    def __init__(self):
        self.amount_of_nodes = 0
        self.adj_list = {}                  # hash table of nodes

    def add_node(self, node):
        if node in self.adj_list:
            return False
        self.adj_list[node] = []         # it's holder for node without connections
        self.amount_of_nodes += 1
        return True

    def add_edge(self, node1, node2):
        if node1 not in self.adj_list or node2 not in self.adj_list:
            return False
        if node2 not in self.adj_list[node1]:
            self.adj_list[node1] += [node2]
        if node1 not in self.adj_list[node2]:
            self.adj_list[node2] += [node1]
        return True



grph = Graph()
grph.add_node(0)
grph.add_node(1)
grph.add_node(2)
grph.add_node(3)
grph.add_node(4)
grph.add_node(5)
grph.add_node(6)

grph.add_edge(3, 1)
grph.add_edge(3, 4)
grph.add_edge(4, 2)
grph.add_edge(4, 5)
grph.add_edge(1, 2)
grph.add_edge(1, 0)
grph.add_edge(0, 2)
grph.add_edge(6, 5)
print(grph.adj_list)