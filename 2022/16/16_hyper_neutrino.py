from collections import deque

valves = {}
tunnels = {}

for line in open("16.in"):
    line = line.strip()
    valve = line.split()[1]
    flow = int(line.split(";")[0].split("=")[1])
    targets = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = targets

# Create an empty dictionary to store the distances from each valve to the valve labeled AA
dists = {}

# Create an empty list to store the non-empty valves (valves with flow rate > 0)
nonempty = []

# Iterate over all the valves in the network
for valve in valves:
    """

    This code is using breadth-first search (BFS) to find the shortest path from each valve to the valve labeled AA. 
    It is storing the distances in the dists dictionary, with the keys being the starting valves and the values being dictionaries of distances to the other valves.
    The nonempty list is being populated with the valves that have a non-zero flow rate. The indices dictionary will be used later in the code to store the indices of each 
    valve in the list of nonempty valves. After the BFS has completed, the code will be able to use the dists dictionary to find the shortest path from any valve to the 
    valve labeled AA, as well as the distance between any two valves in the network.

    """
    # Skip valves with flow rate 0 and the valve labeled AA
    if valve != "AA" and not valves[valve]:
        continue
    
    # Add non-empty valves to the list
    if valve != "AA":
        nonempty.append(valve)

    # Initialize the distances dictionary for this valve
    # with the distance from the valve to itself and AA set to 0
    dists[valve] = {valve: 0, "AA": 0}
    
    # Create a set to store the valves that have been visited
    visited = {valve}
    
    # Create a queue to store the nodes to be visited in the BFS algorithm
    queue = deque([(0, valve)])
    
    # While there are nodes in the queue
    while queue:
        # Get the distance and position (valve) at the front of the queue
        distance, position = queue.popleft()
        
        # Iterate over all the neighbors (connected valves) of the current position
        for neighbor in tunnels[position]:
            # Skip neighbors that have already been visited
            if neighbor in visited:
                continue
            
            # Mark the neighbor as visited
            visited.add(neighbor)
            # add the neighbor to the queue
            queue.append((distance + 1, neighbor))
            # If the neighbor has a non-zero flow rate, add 1 to the distance
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            

    # Remove the distances from the valve to itself and AA from the dictionary
    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

cache = {}

"""

The dfs function will stop when it has explored all possible paths from the starting valve and has 
returned the maximum flow rate that can be achieved within the given time limit.
The function works by starting at a given valve and exploring all of its neighboring valves. 
It does this by recursively calling itself with the remaining time, the neighbor as the current valve, and a updated bitmask representing the valves that have been visited. 
This process continues until all possible paths have been explored, at which point the function returns the maximum flow rate that was achieved along any of the paths.
The function uses a cache to store the results of previous calls so that it does not have to recalculate the same result multiple times. 
This helps to improve the performance of the function by reducing the number of recursive calls that need to be made.
I hope this helps to clarify how the dfs function works. Let me know if you have any further questions or if there is anything else I can assist you with.

"""

def dfs(time, valve, bitmask): # bitmask represents the number of valve opened in binary format
    if (time, valve, bitmask) in cache:
        # If we have, return the previously computed result
        return cache[(time, valve, bitmask)]
    
    maxval = 0
    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            """
            eg: with the 5th valve
            110100 mean that some valve are already open and some not (6 open, 5 open, 4 close, 3 open, ...)
            110100 
        & 
             10000
            -------
            010000 not equal to 0 so it will pass the condition, so, it is not usefull to continue (since it has already been in account)
            
            """
            continue
        remtime = time - dists[valve][neighbor] - 1
        # If there is not enough time remaining to visit the neighbor, skip it
        if remtime <= 0:
            continue
        
        # Recursively call the dfs function to explore the path through the neighbor
        # and add the flow rate of the neighbor multiplied by the remaining time to the maximum value
        maxval = max(maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime) # or in order to add the new valve opened in the cache
        
    cache[(time, valve, bitmask)] = maxval
    return maxval

print(f"Part 1: Maximum flow rate releases: {dfs(30, 'AA', 0)}")
# if we use cache => tmp = max(cache[key] for key in cache)
#   ___     _     ___   _____     ___ 
#  | _ \   /_\   | _ \ |_   _|   |_  )
#  |  _/  / _ \  |   /   | |      / / 
#  |_|   /_/ \_\ |_|_\   |_|     /___|
                                    
b = (1 << len(nonempty)) - 1
# eg: 1111111111111111 final step means that all valves are opened
# 
#  111111111111111
#  001010001100110
#  ---------------
#  110101110011001
#
part_2_max = 0

# In this code, the dfs function is called twice to calculate the maximum pressure that can be released by two workers working together for 26 minutes.
# The first call to dfs computes the maximum pressure that can be released by one worker in 26 minutes, using the bitmask parameter to specify which valves are open.
# The second call to dfs computes the maximum pressure that can be released by the other worke (elephant) in 26 minutes, using the bitmask parameter to specify which valves are 
# closed (b^i).
# The two results are then added together and the maximum value is returned.
# The for loop iterates through all possible combinations of open and closed valves (represented by i), and the maximum pressure released by any combination is stored in part_2_max. 
# Finally, the maximum pressure is printed.

for i in range(b + 1):
    part_2_max = max(part_2_max, dfs(26, 'AA', i) + dfs(26, 'AA', b^i))
"""
The expression b^i is a bitwise XOR operation. It compares the binary representation of b and i and returns a new binary number where each bit is the 
result of the XOR operation between the corresponding bits of b and i.

For example:


b = 15   # binary representation: 1111
i = 7    # binary representation: 0111
b ^ i = 8   # binary representation: 1000

In this case, b and i have 4 and 3 set bits, respectively. The XOR operation compares each bit and returns a 1 if the bits are different and a 0 if they are the same. 
Therefore, the resulting number has one set bit in the fourth position, which corresponds to the only position where b and i have different bits.

In the code you provided, b is a number with all set bits and i is a number with a certain number of set bits. 
The XOR operation is used to get the complement of i, which is a number with all the bits that are not set in i set to 1.

For example:

b = 15   # binary representation: 1111
i = 7    # binary representation: 0111
b ^ i = 8   # binary representation: 1000

In this case, b represents all the valves, and i represents a subset of valves that are already open. 
The XOR operation is used to get the complement of i, which represents all the valves that are not open. This complement is passed to the dfs function, which calculates the 
maximum flow rate for the remaining valves.
The result of the dfs function for the open valves is then added to the result of the dfs function for the remaining valves, to get the total maximum 
flow rate for both sets of valves. This process is repeated for all possible combinations of open and closed valves, and the maximum value is returned as the result.   
"""
print(f"Part 2: Maximum flow rate releases: {part_2_max}")
t=1