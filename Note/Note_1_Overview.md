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
Layer 1: Object-Oriented Programming Basics
Concepts: Classes, Methods, Class Variables, and Exceptions.
Writing Task: Write a brief description of each class and its role within the code.

FileDataLoader:  This class aims to load data from a Txt file about the London underground system when it has passed the parameters about the file address. By

StationInfo: This class aims to store information about The London underground system. By

StationFinder: This class aims to find the path between two stations. 

StationTree: This class aims to create a tree. The tree's root is the start station, and the leaf nodes are the destination station. 

StationNode: This class aims to create the basic unit of the tree. Every station node has its station ID and the neighbour of the node.

StationNotFoundError: This class aims to raise an error when we don't find the station name on the station information. This error gives us specific information about what the error is. 


Layer 2: File Handling and Data Parsing
Concepts: Opening files, reading lines, and splitting strings.
Writing Task: Explain how the FileDataLoader class reads and processes data from a file, specifically how it deals with each line of the file.





Layer 3: Data Storage and Retrieval
Concepts: Dictionaries in Python, Class Methods, and Error Handling.
Writing Task: Describe how StationInfo class stores station information and how its methods facilitate data retrieval, including error handling with StationNotFoundError.


Layer 4: Data Structures and Algorithms
Concepts: Nodes, Trees, and Breadth-First Search (BFS).
Writing Task: Explain how StationNode and StationTree represent stations and their connections. Detail how StationTree.find_path_to_station implements BFS to find a path between two stations.


Layer 5: System Integration and User Interaction
Concepts: System Design, Command Line Interface (CLI), Loops, and Conditionals.
Writing Task: Discuss how the if __name__ == "__main__": block integrates the different components of the system and interacts with the user through the CLI.


The core of our code is structured around several key classes, each responsible for a different aspect of the path-finding system:

AbstractLoadData: An abstract base class defining the interface for loading data.

FileDataLoader: A concrete implementation of AbstractLoadData, responsible for loading station information from a file.

StationInfo: A class holding mappings between station names, IDs, and their neighbours.

StationNode: Represents a station, encapsulating its ID, name, and neighbours.

StationTree: Implements the logic for finding the shortest path between two stations.

StationFinder: Facilitates the high-level functionality of finding paths between stations.

StationNotFoundError: A custom exception class for handling cases where a station is not found.

## Unrequited notes