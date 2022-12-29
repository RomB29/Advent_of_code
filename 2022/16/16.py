from collections import defaultdict
import heapq
import re

filename = "16.in"
file_pattern = "Valve (\w+) has flow rate=(\d+); (tunnels|tunnel) (lead|leads) to (valves|valve) (.*)"

with open(filename, 'r') as f:
    datas = f.read().strip().split('\n')
    
# Data structure to store the graph
graph = defaultdict(list)
# Read the input and build the graph
for line in datas:
    match = re.search(file_pattern, line)
    if match:
        valve_name = match.group(1)
        flow_rate = int(match.group(2))
        connections = match.group(6).strip().split(', ')

    graph[valve_name] = {"flow_rate": flow_rate, "tunnels_connected": connections}


# Function to implement Dijkstra's algorithm
def dijkstra(graph, start, end, time_left):
    # Set of nodes already visited
    visited = set()

    # Priority queue to keep track of the node with the minimum distance
    pq = []
    heapq.heappush(pq, (0, start))

    # Dictionary to store the distance to each node from the start node
    distances = {}

    # Dictionary to store the previous node for each node in the path
    previous = {}

    # While there are nodes in the priority queue
    while pq:
        # Get the node with the minimum distance
        distance, node = heapq.heappop(pq)

        # If we have reached the end node, return the path
        if node == end or time_left == 0:
            path = []
            while node in previous:
                path.append(node)
                node = previous[node]
            path.append(start)
            return path[::-1]

        # If we have already visited this node, skip it
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)

        # Get the flow rate and list of tunnels for this node
        flow_rate, tunnels = graph[node]["flow_rate"], graph[node]["tunnels_connected"] 

        # If there is enough time left, add the flow rate to the distance
        # and explore the neighboring nodes
        if time_left > 0:
            distance += graph[node][flow_rate"]
            time_left -= 1
            for neighbor in tunnels:
                if neighbor not in visited:
                    new_distance = distance
                    if neighbor not in distances or new_distance > distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = node
                        heapq.heappush(pq, (new_distance, neighbor))

    # If we reach here, we have not found a path to the end node
    return []

# Find the shortest path from the start node (AA) to the end node (any node)
# with the maximum flow rate
path = dijkstra(graph, 'AA', None, 30)

# Calculate the maximum pressure release by summing the flow rates of all the
# valves in the path
max_pressure = sum(graph[valve][0] for valve in path)

# Print the result
print(max_pressure)