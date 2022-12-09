import numpy as np
import matplotlib.pyplot as plt
input = open("Day8\Data.txt").read()
treeGrid = np.array([[c for c in row] for row in input.split("\n")])

def draw_plot(arr):
    fig = plt.figure(figsize=(10,10))
    plt.imshow(arr)
    plt.show()

def is_visible(treeGrid, row, column):
    if row == 0 or column == 0 or row == len(treeGrid) - 1 or column == len(treeGrid[row]) - 1: return True
    higher_infront = next(filter(lambda t: t >= treeGrid[row][column], treeGrid[row, column + 1:]), None)
    higher_behind = next(filter(lambda t: t >= treeGrid[row][column], treeGrid[row, :column]), None)
    higher_above = next(filter(lambda t: t >= treeGrid[row][column], treeGrid[:row, column]), None)
    higher_below = next(filter(lambda t: t >= treeGrid[row][column], treeGrid[row + 1:, column]), None)
    if((higher_infront is None or higher_behind is None or higher_above is None or higher_below is None )):
        return True
    else:
        return False

def tree_score(treeGrid, row, column):
    if row == 0 or column == 0 or row == len(treeGrid) - 1 or column == len(treeGrid[row]) - 1: return 0
    arr_infront = list(treeGrid[row, column + 1:])
    arr_behind = list(treeGrid[row, :column])
    arr_behind.reverse()
    arr_above = list(treeGrid[:row, column])
    arr_above.reverse()
    arr_below = list(treeGrid[row + 1:, column])
    higher_infront_pos = next((t for t, val in enumerate(arr_infront) if val >= treeGrid[row][column]), len(arr_infront)) + 1
    higher_behind_pos = next((t for t, val in enumerate(arr_behind) if val >= treeGrid[row][column]), len(arr_behind)) + 1
    higher_above_pos = next((t for t, val in enumerate(arr_above) if val >= treeGrid[row][column]), len(arr_above)) + 1
    higher_below_pos = next((t for t, val in enumerate(arr_below) if val >= treeGrid[row][column]), len(arr_below)) + 1
    if higher_above_pos * higher_behind_pos * higher_below_pos * higher_infront_pos == 733824:
        print()
    return higher_above_pos * higher_behind_pos * higher_below_pos * higher_infront_pos

tree_grid_visibility = [[0 for i in range(len(treeGrid[0]))] for j in range(len(treeGrid))]
tree_grid_score = [[0 for i in range(len(treeGrid[0]))] for j in range(len(treeGrid))]

for i in range(len(treeGrid)):
    for j in range(len(treeGrid[0])):
        tree_grid_visibility[i][j] = is_visible(treeGrid, i, j)

for i in range(len(treeGrid)):
    for j in range(len(treeGrid[0])):
        print(i, j)
        tree_grid_score[i][j] = tree_score(treeGrid, i, j)

#draw_plot(tree_grid_visibility)
print(tree_grid_score)
draw_plot(tree_grid_score)
print("Answer to Q1: {}".format(np.count_nonzero(tree_grid_visibility)))
print("Answer to Q2: {}".format(np.max(tree_grid_score)))
