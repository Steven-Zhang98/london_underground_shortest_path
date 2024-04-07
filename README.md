# LondonUndergroundShortestPath

## Introduction to the System
In this project, we'll explore the London Underground, the oldest underground railway network in the world. The system's complexity creates a significant need for an efficient route-finding way to help passengers find the path between stations. 

## Usage Instructions
To bring this innovative solution to the hands of users, we outline simple steps for setup and operation:

Setup: Download the source code and open it with a code editor like PyCharm.
Running the Application: Execute the main.py script to interact with the system via prompts or launch UIVersion for a graphical interface.

Customisation: Users can personalise their experience by modifying the stations.txt file and adjusting UI elements like fonts and backgrounds to suit their preferences.
## Overview of the Code Structure

The core of our code is structured around several key classes, each responsible for a different aspect of the path-finding system:

AbstractLoadData: An abstract base class defining the interface for loading data.

FileDataLoader: A concrete implementation of AbstractLoadData, responsible for loading station information from a file.

StationInfo: A class holding mappings between station names, IDs, and their neighbours.

StationNode: Represents a station, encapsulating its ID, name, and neighbours.

StationTree: Implements the logic for finding the shortest path between two stations.

StationFinder: Facilitates the high-level functionality of finding paths between stations.

StationNotFoundError: A custom exception class for handling cases where a station is not found.

## Detailed Explanation of the Code

Data Loading: Our journey begins with FileDataLoader, a class responsible for ingesting station information from a file. It parses each line to map station names to their IDs and neighbors, populating the StationInfo class for easy retrieval.
Station Representation: The StationNode class encapsulates a station, linking its name, ID, and neighboring stations. This node is pivotal for traversing the network.
Path Finding: The StationTree takes the spotlight as it embarks on a quest to find the shortest path between stations. Utilizing a breadth-first search algorithm, it explores connections until it reaches the destination.
User Interaction: Finally, the StationFinder bridges the gap between backend logic and user commands, offering an intuitive interface for querying paths.

## Technical Concepts and Algorithms

Underpinning our system are key technical concepts and algorithms crucial for its efficiency:

Abstract Base Classes (ABCs): By employing ABCs, we ensure that our data loading mechanism is extensible, paving the way for different data sources in the future.
Breadth-First Search (BFS): The choice of BFS for path finding is no coincidence. Its ability to find the shortest path in unweighted graphs like our station network makes it the perfect fit.

## Challenges and Solutions

## Conclusion and Further Exploration

## References and Further Reading


### To-Do list
- 参考范范笔记（链接）形成前端和代码解释[GitHub - ShiyuFan0820/ShortestPathInLondonUnderground](https://github.com/ShiyuFan0820/ShortestPathInLondonUnderground/tree/main)
