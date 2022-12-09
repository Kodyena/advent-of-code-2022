import numpy as np
import math
import matplotlib.pyplot as plt
class StringKnot:
    def __init__(self, no_of_tails):
        if no_of_tails != 0:
            self.tail = StringKnot(no_of_tails - 1)
        else: 
            self.tail = None
        self.pos = np.array([0,0])
        self.positions = list()
        self.positions.append(self.pos.copy())

    def __repr__(self) -> str:
        return "head position: {}, tail position: {}.".format(self.pos, self.tail_pos)

    def __str__(self) -> str:
        return self.__repr__()

    def move_head(self, direction, spaces):
        dir = [0,0]
        dir[0] += {'R': 1, 'L': -1}.get(direction, 0)
        dir[1] += {'D': -1, 'U': 1}.get(direction, 0)
        
        for i in range(spaces):
            self.pos += np.array(dir)
            self.positions.append(self.pos.copy())
            self.update_tail()

    def move(self, correction):
        self.pos += np.array(correction)
        self.positions.append(self.pos.copy())
        self.update_tail()
        
    def head_tail_signed_distance(self):
        return self.pos - self.tail.pos
    
    def update_tail(self):
        if self.tail != None:
            distance = self.head_tail_signed_distance()
            if(np.linalg.norm(distance) > 1.5):
                correction  = [sign(n) * min(abs(n), 1) for n in distance]
                self.tail.move(correction)

    def get_sub_tail(self, index):
        tail = self.tail
        for i in range(index - 1):
            if(tail == None):
                return None
            else:
                tail = tail.tail
        return tail
    
def sign(int) -> int:
    if int < 0:
        return -1
    else:
        return 1

def draw_plot(arr):
    fig = plt.figure(figsize=(10,10))
    plt.imshow(arr)
    plt.show()            
            
commands  = [[c for c in line.split(" ")] for line in open("Day9\Data.txt").read().split("\n")]
string = StringKnot(9)

for command in commands:
    string.move_head(command[0], int(command[1]))

tail_index = 9

# grid_min_x = min(string.get_sub_tail(tail_index).positions, key=lambda l: l[0])[0]
# grid_max_x = max(string.get_sub_tail(tail_index).positions, key=lambda l: l[0])[0]
# grid_min_y = min(string.get_sub_tail(tail_index).positions, key=lambda l: l[1])[1]
# grid_max_y = max(string.get_sub_tail(tail_index).positions, key=lambda l: l[1])[1]
# grid_plot = [[0 for j in range(grid_min_y, grid_max_y)] for i in range(grid_min_x, grid_max_x)]

# for pos in string.get_sub_tail(tail_index).positions:
#     x = pos[0] - grid_min_x - 1
#     y = pos[1] - grid_min_y - 1
#     grid_plot[x][y] += 1

#draw_plot(grid_plot)

print("Total positions {}".format(len(string.get_sub_tail(1).positions)))
print("Answer to Q1: {}".format(len(np.unique(string.get_sub_tail(1).positions, axis=0))))
print("Answer to Q1: {}".format(len(np.unique(string.get_sub_tail(9).positions, axis=0))))