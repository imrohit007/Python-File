#A program to find the shortest path between two nodes in a graph
import sys

def dijkstra(graph, start, end):
    # Set up distance and predecessor dictionaries
    distances = {}
    predecessors = {}

    # Set all distances to infinity and all predecessors to None
    for node in graph:
        distances[node] = sys.maxsize
        predecessors[node] = None

    # Set the distance to the start node to 0
    distances[start] = 0

    # Create a set of unvisited nodes
    unvisited_nodes = set(graph.keys())

    # While there are unvisited nodes
    while unvisited_nodes:
        # Find the node with the smallest distance
        current_node = None
        smallest_distance = sys.maxsize
        for node in unvisited_nodes:
            if distances[node] < smallest_distance:
                current_node = node
                smallest_distance = distances[node]

        # If we have reached the end node, we are done
        if current_node == end:
            break

        # Remove the current node from the set of unvisited nodes
        unvisited_nodes.remove(current_node)

        # Update the distances of the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor through the current node
            distance = distances[current_node] + weight
            # If the distance to the neighbor through the current node is smaller than the current distance, update the distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node

    # Build the shortest path by following the predecessors from the end node
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]

    # Reverse the path to get the correct order
    path = path[::-1]

    return path

# Example usage

# Define the graph as a dictionary where the keys are the nodes and the values are the neighbors and their weights
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 2, 'E': 3},
    'C': {'D': 4, 'F': 5},
    'D': {'E': 1},
    'E': {'F': 1},
    'F': {}
}

# Find the shortest path from node A to node F
shortest_path = dijkstra(graph, 'A', 'F')

print(shortest_path)
