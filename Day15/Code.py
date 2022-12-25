import re
import math

class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"X: {self.x} Y: {self.y}"
    def __str__(self) -> str:
        return self.__repr__()
    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.self)
    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)
    def manhattan_distance(self, other):
        delta = self - other
        return abs(delta.x) + abs(delta.y)

class SensorMap():

    def __init__(self, sensor_to_beacon):
        self.sensor_to_beacon = sensor_to_beacon
        self.sensor_ranges = {s: s.manhattan_distance(b) for s, b in sensor_to_beacon.items()}

    def __repr__(self):
        print("Sensor Position: {}, Beacon Position: {}".format(self.sensor_pos, self.beacon_pos))

    def __str__(self) -> str:
        print(self.__repr__())

    def get_row_range(self, row):
        if(abs(self.sensor_pos[1] - row) > self.distance):
            return []

        vert_distance_to_tile = abs(self.sensor_pos[1] - row)
        hori_distance_row = self.distance - vert_distance_to_tile
        return range(self.sensor_pos[0] - hori_distance_row, self.sensor_pos[0] + hori_distance_row)

    def get_blocked_ranges(self, row):
        blocked_positions = list()
        for sensor, sensor_range in self.sensor_ranges.items():
            vert_distance_to_tile = abs(sensor.y - row)
            if(vert_distance_to_tile < sensor_range):
                hori_distance_to_tile = sensor_range - vert_distance_to_tile
                blocked_positions.append(range(sensor.x - hori_distance_to_tile, sensor.x + hori_distance_to_tile))

        return self.merge_range_list(blocked_positions)

    def merge_range_list(self, ranges):
        ranges.sort(key = lambda x: x.start)
        merged_ranges = list()
        merged_ranges.append(ranges[0])
        
        for interval in ranges[1:]:
            if(interval.start <= merged_ranges[-1].stop):
                if(interval.stop > merged_ranges[-1].stop):
                    merged_ranges[-1] = range(merged_ranges[-1].start, interval.stop)
            else:
                merged_ranges.append(interval)

        return merged_ranges

    #Part 2
    def coord_to_tuning_freq(coord):
        return coord.x * 4000000 + coord.y
    
    def get_beacon_tuning_freq(self):
        for j in range(4000000):
            blocked_ranges = self.get_blocked_ranges(j)

            if(len(blocked_ranges) > 1):
                for interval in blocked_ranges:
                    if(0 < interval.stop + 1 < 4000000):
                        return self.coord_to_tuning_freq(Coord(interval.stop + 1, j))
        
        return 0


with open("Day15\Data.txt") as f:
    locations = [[int(n) for n in re.findall(r'-?\d+', line)] for line in f.read().split("\n")]
    sensor_beacon_pairs = {Coord(location_pair[0], location_pair[1]): Coord(location_pair[2], location_pair[3]) for location_pair in locations}

sensor_map = SensorMap(sensor_beacon_pairs)

blocked_positions = sensor_map.get_blocked_ranges(2000000)
amount_of_blocked_positions = sum(map(lambda interval: interval.stop - interval.start, blocked_positions))
print("Answer to Q1: {}".format(amount_of_blocked_positions))

print("Answer to Q2: {}".format(sensor_map.get_beacon_tuning_freq()))


            