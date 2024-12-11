import random

class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}  # Distance to all other nodes
        self.neighbors = []  # Neighbor nodes

    def add_neighbor(self, neighbor, distance):
        self.neighbors.append((neighbor, distance))
        self.routing_table[neighbor.name] = (distance, neighbor.name)

    def update_routing(self):
        changes = False
        for neighbor, distance in self.neighbors:
            # For each neighbor, update the routing table
            for destination, (distance_from_neighbor, next_hop) in neighbor.routing_table.items():
                new_distance = distance + distance_from_neighbor
                if destination not in self.routing_table or new_distance < self.routing_table[destination][0]:
                    self.routing_table[destination] = (new_distance, neighbor.name)
                    changes = True
        return changes

    def print_routing_table(self):
        print(f"Routing table of {self.name}:")
        for destination, (distance, next_hop) in self.routing_table.items():
            print(f"Destination: {destination}, Distance: {distance}, Next hop: {next_hop}")
        print()

