import math

class Point:
    def __add__(self, other: int):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Point):
            return False
        return self.x == __o.x and self.y == __o.y

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __str__(self):
        return self.__repr__()
    

class Tetrad:
    def __init__(self, shape, position: Point = Point(0, 0)):
        #Points are defined from position
        self.points = set(shape)
        self.position = position
        self.horizontal_size = max([p.x for p in self.points]) + 1
        self.vertical_size = max([p.y for p in self.points]) + 1

    def get_points_on_grid(self, point_shift=Point(0, 0)):
        return set([p + self.position + point_shift for p in self.points])

    def is_blocked_right(self, points: set):
        if(len(points) == 0): return False
        return not set(points).isdisjoint(self.get_points_on_grid(Point(1, 0)))

    def is_blocked_left(self, points: set):
        if(len(points) == 0): return False
        return not set(points).isdisjoint(self.get_points_on_grid(Point(-1, 0)))

    def is_blocked_below(self, points: set):
        if(len(points) == 0): return False
        return not set(points).isdisjoint(self.get_points_on_grid(Point(0, -1)))

class Tetris:
    settled: set

    tetrad_shapes = [[[1, 1, 1, 1]], 
                     [[0, 1, 0],
                      [1, 1, 1],
                      [0, 1, 0]],
                     [[1, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1]],
                     [[1],
                      [1], 
                      [1],
                      [1]],
                     [[1, 1], 
                      [1, 1]]]

    tetrad_points = [[Point(i, j) for j in range(len(shape)) for i in range(len(shape[0])) if shape[j][i] == 1] for shape in tetrad_shapes]
    
    def drop_tetrad(self, tetrad: Tetrad, move_iter):
        start_y = 4
        if(len(self.settled) != 0):
            start_y = max([p.y for p in self.settled]) + 4
        
        start_x = 2
        tetrad.position = Point(start_x, start_y)

        for move in move_iter:
            if(move == '<' and tetrad.position.x != 0 and not tetrad.is_blocked_left(self.settled)):
                tetrad.position -= Point(1, 0)
            elif(move == '>' and tetrad.position.x + tetrad.horizontal_size - 1 != self.grid_width - 1 and not tetrad.is_blocked_right(self.settled)):
                tetrad.position += Point(1, 0)

            #drop and check
            tetrad.position -= Point(0, 1)
            tetrad_points = set([p + tetrad.position for p in tetrad.points])

            if not tetrad_points.isdisjoint(self.settled) or 0 in [p.y for p in tetrad_points]:
                #stop tetrad
                new_settled = [p + Point(0, 1) for p in tetrad_points]
                self.settled.update(set(new_settled))
                return True

        return False

    def drop_n_tetrads(self, n, moves):
        move_iter = iter(moves)
        for i in range(n):
            self.drop_tetrad(Tetrad(self.tetrad_points[i % 5]), move_iter)
            self.draw_grid()
    
    def draw_grid(self, tetrad: Tetrad = None):
        highest_point = Point(0, 0)
        tetrad_points = list()
        if(tetrad != None):
            tetrad_points = tetrad.get_points_on_grid()
            highest_point = max(tetrad_points, key=lambda p: p.y)
        elif(len(self.settled) > 0):
            highest_point = max(self.settled, key=lambda p: p.y)
            
        grid_str = ''
        for j in range(highest_point.y + 1, 0, -1):
            for i in range(self.grid_width):
                
                if self.point_in_list(i, j, self.settled) or Point(i, j) in tetrad_points:
                    grid_str += '#'
                else:
                    grid_str += '-'
            grid_str += '\n'
        
        print(grid_str)

    def point_in_list(self, x, y, check_list):
        for point in check_list:
            if(point.x == x and point.y == y):
                return True
        
        return False

    def __init__(self, width):
        self.grid_width = width
        self.settled = set()




sample_jets = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
jets = open("Day17\Data.txt").read()
tetris = Tetris(7)
tetris.drop_n_tetrads(10, sample_jets)