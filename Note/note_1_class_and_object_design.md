---
in: 
up: 
down: 
related: 
opposite: 
by: 
created: 2024-04-07T00:00:00
due-date: 2024-04-08
rank: 
tags:
---
## Data Storage and access

- Firstly, the system uses the **FileDataLoader** class to load subway station information from a text file, including station ID, name, and neighbouring stations.

- The **StationInfo class** aims to provide an interface for querying station information, such as obtaining an ID based on the station name, retrieving the station name based on the ID, and getting a list of neighbouring station IDs. This design pattern, which **separates** data access from data storage, helps improve code maintainability and scalability.

- Core function, which includes the StationNode and StationTree classes. The StationNode class has basic information about a station, such as its name, ID, and connected neighbouring stations. The StationTree class use the Breadth-First Search (BFS) algorithm to find the shortest path between two stations. 

- User Interface: the StationFinder class and the main function provide the user interface, allowing users to input the start and end stations and then display the path between these two stations.

- Error Handling: Using exception StationNotFoundError to manage cases where a queried station does not exist. 

