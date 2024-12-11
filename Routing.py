import networkx as nx
import matplotlib.pyplot as plt

class Routing:
    def __init__(self):
        pass

    def routing_simulation(self, nodes, iterations=10):
        for i in range(iterations):
            print(f"Iteration {i + 1}:")
            changes = False
            for node in nodes:
                if node.update_routing():
                    changes = True
            if not changes:
                break
            # Print routing tables after each iteration
            for node in nodes:
                node.print_routing_table()

    def draw_network(self, nodes):
        G = nx.Graph()  # Create an undirected graph
        
        # Add nodes and connections (edges)
        for node in nodes:
            G.add_node(node.name)  # Add the node
        
        for node in nodes:
            for neighbor, distance in node.neighbors:
                # Add the connection (edge) between the node and its neighbor
                G.add_edge(node.name, neighbor.name, weight=distance)
        
        # Draw the graph
        pos = nx.spring_layout(G)  # Layout for node positioning
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold")
        
        # Add weights (distances) on the connections
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        # Show the graph
        plt.title("Routing Network")
        plt.show()
