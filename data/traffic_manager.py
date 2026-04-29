import json
import os

class TrafficManager:
    def __init__(self, blocked_path=None):
        if blocked_path is None:
            self.blocked_path = os.path.join(os.path.dirname(__file__), "processed_data", "blocked_edges.json")
        else:
            self.blocked_path = blocked_path
            
        self.blocked_edges = self._load_blocked_edges()

    def _get_edge_key(self, u, v):
        # Đảm bảo (A, B) và (B, A) là một
        return tuple(sorted((u, v)))

    def _load_blocked_edges(self):
        if os.path.exists(self.blocked_path):
            try:
                with open(self.blocked_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return set(tuple(edge) for edge in data)
            except Exception:
                return set()
        return set()

    def _save(self):
        with open(self.blocked_path, "w", encoding="utf-8") as f:
            json.dump([list(edge) for edge in self.blocked_edges], f, ensure_ascii=False, indent=2)

    def block(self, u, v):
        edge = self._get_edge_key(u, v)
        self.blocked_edges.add(edge)
        self._save()

    def unblock(self, u, v):
        edge = self._get_edge_key(u, v)
        if edge in self.blocked_edges:
            self.blocked_edges.remove(edge)
            self._save()

    def is_blocked(self, u, v):
        return self._get_edge_key(u, v) in self.blocked_edges