from Node import Node
from Routing import Routing

class Main:
    def __init__(self):
        self.routing = Routing()

    def start(self):
        # Nodes creation
        node_a = Node("A")
        node_b = Node("B")
        node_c = Node("C")
        node_d = Node("D")

        # Adding neighbors (and relative distances)
        node_a.add_neighbor(node_b, 1)
        node_a.add_neighbor(node_c, 4)

        node_b.add_neighbor(node_a, 1)
        node_b.add_neighbor(node_c, 2)
        node_b.add_neighbor(node_d, 5)

        node_c.add_neighbor(node_a, 4)
        node_c.add_neighbor(node_b, 2)
        node_c.add_neighbor(node_d, 1)

        node_d.add_neighbor(node_b, 5)
        node_d.add_neighbor(node_c, 1)

        # List of all nodes in the network
        nodes = [node_a, node_b, node_c, node_d]

        # Drawing the network
        self.routing.draw_network(nodes)

        # Routing simulation
        self.routing.routing_simulation(nodes)

if __name__ == "__main__":
    Main().start()