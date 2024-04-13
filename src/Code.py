class FileDataLoader():
	def __init__(self,filename) -> None:
		self.m_filename = filename

	def load_data(self):
		with open(self.m_filename, 'r') as file:
			for line in file:
				parts = line.strip().split('|')  # split line in to parts and strip extra spaces
				if len(parts) >= 3:  # Ensure there are at least 3 parts in the line
					station_id = parts[0]
					station_name = parts[1]
					station_neighbor = parts[2]
					StationInfo.m_name_to_id[station_name] = station_id   # station_id rather than id 
					StationInfo.m_id_to_name[station_id] = station_name    		
					StationInfo.m_id_to_neighbor[station_id] = station_neighbor.strip().split(',')  # split neighbor string into a list
				else:
					print(f"Skipping malformed line: {line.strip()}")


class StationInfo:
	m_name_to_id = {}
	m_id_to_name = {}
	m_id_to_neighbor = {}

	@classmethod				
	def get_id_from_name(cls, staion_name):
		try:
			return cls.m_name_to_id[staion_name]
		except KeyError:
			raise StationNotFoundError(f"station {staion_name} not found")

	@classmethod
	def get_name_from_id(cls, station_id):
		try:
			return cls.m_id_to_name[station_id]
		except KeyError:
			raise StationNotFoundError(f"station {station_id} not found")

	@classmethod
	def get_neighbor_ids_from_id(cls, station_id):
		try:
			return cls.m_id_to_neighbor[station_id]
		except KeyError:
			raise StationNotFoundError()

class StationNode:
	def __init__(self, name: str):
		self.m_node_name = name  
		self.m_node_id = StationInfo.get_id_from_name(name)
		self.m_node_neighbor_ids = StationInfo.get_neighbor_ids_from_id(self.m_node_id)
	
	def get_name(self):
		return self.m_node_name
	
	def get_id(self):
		return self.m_node_id
		
	def get_neighbor_ids(self):
		return self.m_node_neighbor_ids
	
class StationTree:
	def __init__(self, from_station_node: StationNode):
		self.m_root = from_station_node
	
	def find_path_to_station(self, to_station_node: StationNode):
		station_queue = [(self.m_root.get_id(), [self.m_root.get_id()])]
		visited = set()
		while station_queue:
			cur_node_id, path = station_queue.pop(0)
			if cur_node_id in visited:   # Compare node identifiers rather than node objects themselves
				continue
			visited.add(cur_node_id)
			if cur_node_id == to_station_node.get_id():
				return path
			for neighbor_id in StationInfo.get_neighbor_ids_from_id(cur_node_id):
				if neighbor_id not in visited:
					station_queue.append((neighbor_id, path + [neighbor_id]))	
			
class StationFinder:
	def __init__(self) -> None:

	def get_path(self, from_station:str, to_station:str):
		from_station_node = StationNode(from_station)
		to_station_node = StationNode(to_station)
		tree = StationTree(from_station_node)
		path_ids = tree.find_path_to_station(to_station_node)
		path_names = [StationInfo.get_name_from_id(station_id) for station_id in path_ids]
		return path_names
	
class StationNotFoundError(Exception):
	"""Exception raised when a station is not found."""
    
if __name__ == "__main__":
	station_txt = FileDataLoader('/Users/zhangxiyun/LondonPath/stations.txt')
	finder = StationFinder(station_txt)
	while True:
		from_station = input("please input you start station:")
		to_station = input("please input you terminal station:")
		if from_station == "exit" or to_station == "exit":
			break
		try:
			path = finder.get_path(from_station, to_station)
			print(path)
		except StationNotFoundError as e:
			print(e)
		
