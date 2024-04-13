## Data Structures

### Dictionaries
The StationInfo class uses dictionaries (m_name_to_id, m_id_to_name, m_id_to_neighbor) to store station names, IDs, and neighbouring station information. This choice is strategic for several reasons:

1. mapping the relationship: Dictionaries directly map keys to values (like station IDs or names) with specific data (like neighbouring station IDs).

### Lists
In the StationNode and StationTree classes, lists are used to store the IDs of neighbouring stations (m_node_neighbor_ids) and to manage the queue for the breadth-first search algorithm (station_queue). Lists are appropriate here because:

1. Dynamic resizing: Lists in Python provide flexibility when I don’t know the exact number of elements in advance, such as the varying number of neighbours or path length in me routing algorithm.
2. Ease of iteration: Lists provide an easy way to iterate over elements, which is useful when I need to process each neighbour of a station or each node in a path sequentially.
###  Sets
The visited set in the StationTree class is used to track which stations have been visited during the search for a path. Sets are particularly well-suited for this purpose because:

1. O(1) average-time complexity for lookups: This data structure is very useful when quickly determining if a node has already been explored to prevent reprocessing.
### Queues
The queue is a logical data structure, and the list used as station_queue in the StationTree class acts as a queue. 
1. first-in-first-out (FIFO) data structure: to ensure nodes are processed in the order they are discovered.

## Algorithms
### Breadth-First Search (BFS):
Usage: Implemented in the StationTree class to find the shortest path from a starting station to a destination station.
Reason: BFS is ideal for finding the shortest path in unweighted graphs and is the network of stations where all connections are considered equal. BFS explores all neighbours at the present depth before moving on to nodes at the next depth level, ensuring the shortest path is found in the least number of steps.