import sys
import os
sys.path.append(os.path.abspath('../..'))

from data.data_loader import GraphData
import heapq


def ucs(data: GraphData, src: str, des: str) -> dict:
    
    # Validate
    if not data.has_node(src):
        print(f"[UCS] Unknown station: '{src}'")                    # UPDATE ERROR LOG
        return None
    if not data.has_node(des):
        print(f"[UCS] Unknown station: '{des}'")                    # UPDATE ERROR LOG
        return None
    if src == des:
        return {"path": [src], "cost": 0.0, "explored": []}         # UPDATE ORDER 
    
    # Data structures
    fringe = [(0.0, src)]   # g(n), station
    
    closed = set()          
    save_path = {}          # station -> prev station
    explored = []

    #loop:
    while fringe:
    #   take out lowest cost in fringe
        cost, current = heapq.heappop(fringe)
        closed.add(current)
        explored.append(current)

    #   if current = destination -> end loop, return path
        if current == des: 
            # retrace path
            path = [current]
            while not current == src:
                current = save_path[current]
                path.append(current)

            return {"path": list(reversed(path)),
                    "cost": round(cost, 4), 
                    "explored": explored}                           # UPDATE ORDER 
        
    #   push neighbors into fringe
        for v, e in data.get_neighbors(current):
            if v in closed:
                continue

            heapq.heappush(fringe, (cost + e, v))
            save_path[v] = current

    #   no more in fringe -> return none
    return None

#####test
result = ucs("Central", "Hung Hom")
print(result)