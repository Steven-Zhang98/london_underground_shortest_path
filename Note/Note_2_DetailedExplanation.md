Data Loading: Our journey begins with FileDataLoader, a class responsible for ingesting station information from a file. It parses each line to map station names to their IDs and neighbors, populating the StationInfo class for easy retrieval.

Station Representation: The StationNode class encapsulates a station, linking its name, ID, and neighboring stations. This node is pivotal for traversing the network.123

Path Finding: The StationTree takes the spotlight as it embarks on a quest to find the shortest path between stations. Utilizing a breadth-first search algorithm, it explores connections until it reaches the destination.
1342
User Interaction: Finally, the StationFinder bridges the gap between backend logic and user commands, offering an intuitive interface for querying paths.


