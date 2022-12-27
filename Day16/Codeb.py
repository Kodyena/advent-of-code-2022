import re 
from functools import lru_cache
from collections import deque 
class Valve:
    def __init__(self, data):
        self.name = data[0]
        self.flow_rate = int(data[1])
        self.connected_valves = data[2:]
        self.is_open = False
    
    def __repr__(self) -> str:
        return f'Name: {self.name}, Flow: {self.flow_rate}, Open: {self.is_open}'
    
    def __str__(self) -> str:
        return self.__repr__()


class ValveGraph:
    #Do highest valves first

    def __init__(self, data):
        self.valve_connections: dict[Valve, list[Valve]] = dict()
        for datum in data:
            valve = Valve(datum)
            self.valve_connections[valve] = valve.connected_valves
        self.name_to_valve = { valve.name : valve for valve in self.valve_connections.keys()}
        self.valve_flow_rates = {v : v.flow_rate for v in self.valve_connections.keys()}

    @lru_cache(maxsize=None)
    def time_to_open_valve(self, v0, v1):
        #Perform breadth first search
        queue = deque([[v0]])
        visited = set()

        if v0 == v1:
            return 0

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node not in visited:
                connected = node.connected_valves

                for conn_valve in connected:
                    new_path = list(path)
                    new_path.append(self.name_to_valve[conn_valve])
                    queue.append(new_path)

                    if(conn_valve == v1.name):
                        return len(new_path) 

                visited.add(node)
        return None

    def get_best_flow_rate(self, minutes: int):
        #get all paths and then join all disjoint sets
        paths = list()
        max_path = {}
        max_flow = 0
        current_valve = self.name_to_valve["AA"]
        valves = [valve[0] for valve in self.valve_flow_rates.items() if valve[1] > 0]
        q = deque([([current_valve], minutes, {})])
        
        while q:
            path, time, valve_open_time = q.pop()
            if time <= 0 or len(path) == len(valves) + 1:
                paths.append([valve_open_time, sum(map(lambda x: x[0].flow_rate * max(x[1], 0), valve_open_time.items()))])
            else:
                for valve in valves:
                    if valve not in valve_open_time.keys():
                        time_left = time - self.time_to_open_valve(path[-1], valve) 
                        new_valve_open_time = dict(valve_open_time)
                        new_valve_open_time[valve] = time_left
                        q.append((path + [valve], time_left, new_valve_open_time))

        print("got all paths")
        #sort by flow
        paths.sort(key=lambda p: p[1], reverse=True)
        for valve_path_one, flow_one in paths:
            if(flow_one + paths[0][1] < max_flow):
                return max_flow
            for valve_path_two, flow_two in paths:
                total_flow = flow_one + flow_two
                if(total_flow < max_flow):
                    break
                if(valve_path_one.keys().isdisjoint(valve_path_two.keys()) and total_flow > max_flow):
                    max_flow = total_flow
        
    def flow_per_minute(self, open_valves):
        flow_released = 0
        for valve in open_valves:
            flow_released += valve.flow_rate
        
        return flow_released
       
with open("Day16\Data.txt") as f:
    valves = [re.findall(r'[A-Z]{2}|[0-9]+', line) for line in f.read().splitlines()]

graph = ValveGraph(valves)
max_flow = graph.get_best_flow_rate(26)
print(f"Answer to Q2: {max_flow}")