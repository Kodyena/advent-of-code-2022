import math

class Point:
    def __add__(self, other: int):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self, x, y):
            return(f"({x}, {y})")
    
    def __str__(self):
        return self.__repr__()
    
class Tetrad:
    def __init__(self, shape, position: Point = Point(0, 0)):
        self.points = set(shape)
        self.position = position
        self.horizontal_size = max([p.x for p in self.points]) + 1
        self.vertical_size = max([p.y for p in self.points]) + 1

class Tetris:
    settled: set

    tetrad_shapes = [[[1, 1, 1, 1]], 
                     [[0, 1, 0],
                      [1, 1, 1],
                      [0, 1, 0]],
                     [[0, 0, 1],
                      [0, 0, 1],
                      [1, 1, 1]],
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
            if(move == '<' and tetrad.position.x != 0):
                tetrad.position -= Point(1, 0)
            elif(move == '>' and tetrad.position.x + tetrad.horizontal_size - 1 != self.grid_width - 1):
                tetrad.position += Point(1, 0)

            #drop and check
            tetrad.position -= Point(0, 1)
            tetrad_points = set([p + tetrad.position for p in tetrad.points])

            if not tetrad_points.isdisjoint(self.settled) or tetrad.position.y == 0:
                #stop tetrad
                self.settled.update(set([p + Point(0, 1) for p in tetrad_points]))
                return True

        return False

    def drop_n_tetrads(self, n, moves):
        move_iter = iter(moves)
        for i in range(n):
            self.drop_tetrad(Tetrad(self.tetrad_points[i % 4]), move_iter)
            self.draw_grid()
    
    def draw_grid(self):
        highest_point = max(self.settled, key=lambda p: p.y)
        grid_str = ''
        for j in range(highest_point.y + 1, 0, -1):
            for i in range(self.grid_width):
                
                if self.point_in_list(i, j, self.settled):
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





jets = open("Day17\Data.txt").read()
tetris = Tetris(7)
tetris.drop_n_tetrads(2, jets)