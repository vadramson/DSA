# Python Implementation of Graph

from collections import defaultdict

class Graph():
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = defaultdict(list) # self.graph_dict = {}
        
        
        for k, v in self.edges: # Build a dictionary of 
            self.graph_dict[k].append(v) # adds values V to keys K if exist or adds an empty list
        self.graph_dict = dict(self.graph_dict)
        print(self.graph_dict)
        
    
    def get_path(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for stops in self.graph_dict[start]:
            # print(stops) # => Iteratively prints Douala then Paris
            if stops not in path:
                new_paths = self.get_path(stops,end,path) # Recursively Calls the get_path method with Douala then Paris as start and by so doing adding them to path[]. First iteration ends when start == end
                for i in new_paths:
                    paths.append(i)
        return paths            
        
        
    def get_shortest_path(self, start, end):
        return min(self.get_path(start, end))



if __name__ == '__main__':
    city_stops = [
                ("Douala", "Paris"),
                ("Douala", "Dakar"),
                ("Paris", "Dakar"),
                ("Paris", "New York"),
                ("Dakar", "New York"),
                ("New York", "Boston")
                ]
    
    graph = Graph(city_stops)
    
    start, end = "Douala", "New York"
    print(f"Path from {start} to {end} is" ,graph.get_path(start, end))
    print(f"The shortest path from {start} to {end} is",graph.get_shortest_path(start, end))
    
