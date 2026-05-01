import json
import os
import math
from .traffic_manager import TrafficManager

class GraphData:
    def __init__(self, graph_path=None, coords_path=None):
        if graph_path is None:
            graph_path = os.path.join(os.path.dirname(__file__), "processed_data", "graph.json")
        if coords_path is None:
            coords_path = os.path.join(os.path.dirname(__file__), "processed_data", "coords.json")
        
        with open(graph_path, "r", encoding="utf-8") as f:
            self.graph = json.load(f)

        with open(coords_path, "r", encoding="utf-8") as f:
            self.coords = json.load(f)

        self.traffic = TrafficManager()

    def get_nodes(self):
        return list(self.graph.keys())
    
    def has_node(self, node):
        return node in self.graph
    
    def get_neighbors(self, node):
        all_neighbors = self.graph.get(node, [])
        return [
            [neighbor, cost] for neighbor, cost in all_neighbors 
            if not self.traffic.is_blocked(node, neighbor)
        ]

    def get_cost(self, u, v):
        for neighbor, cost in self.graph.get(u, []):
            if neighbor == v:
                return cost
        return float("inf")

    
    def get_coord(self, node):
        return self.coords.get(node, None)

    
    def heuristic(self, a, b):
        R = 6371  
        lat1, lon1 = self.get_coord(a)
        lat2, lon2 = self.get_coord(b)  
        lat1, lon1 = math.radians(lat1), math.radians(lon1)
        lat2, lon2 = math.radians(lat2), math.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        return R * c

    def get_all_edges(self):
        """Return all edges as a list of (u, v, cost) without duplicates."""
        edges = []
        seen = set()
        for u, neighbors in self.graph.items():
            for v, cost in neighbors:
                edge_key = tuple(sorted((u, v)))
                if edge_key not in seen:
                    seen.add(edge_key)
                    edges.append((u, v, cost))
        return edges

    def get_blocked_edges(self):
        """Return list of currently blocked edges."""
        return [list(edge) for edge in self.traffic.blocked_edges]

    def block_station_path(self, u, v):
        self.traffic.block(u, v)

    def unblock_station_path(self, u, v):
        self.traffic.unblock(u, v)
