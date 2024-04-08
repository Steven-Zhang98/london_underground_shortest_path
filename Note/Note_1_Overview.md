The core of our code is structured around several key classes, each responsible for a different aspect of the path-finding system:
范范是憨包
AbstractLoadData: An abstract base class defining the interface for loading data.

FileDataLoader: A concrete implementation of AbstractLoadData, responsible for loading station information from a file.

StationInfo: A class holding mappings between station names, IDs, and their neighbours.

StationNode: Represents a station, encapsulating its ID, name, and neighbours.

StationTree: Implements the logic for finding the shortest path between two stations.

StationFinder: Facilitates the high-level functionality of finding paths between stations.

StationNotFoundError: A custom exception class for handling cases where a station is not found.