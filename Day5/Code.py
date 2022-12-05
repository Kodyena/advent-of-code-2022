get_top_boxes = lambda b: ''.join([b[i][0]for i in range(len(boxes))])

def move_boxes(boxes, amount_to_move, stack_from, stack_to, reverse):
    boxesToMove = boxes[stack_from][0:amount_to_move]
    boxes[stack_from] = boxes[stack_from][amount_to_move:]
    if reverse: boxesToMove.reverse()
    boxesToMove.extend(boxes[stack_to])
    boxes[stack_to] = boxesToMove 

with open("Day5\Boxes.txt") as f:
    lines = [[line[i] for i in range(1, len(line) - 1, 4)] for line in f.read().split("\n")]
    boxes = [list(''.join(list(i)).replace(' ', '')) for i in zip(*lines)]

boxes_one = list(boxes)
boxes_two = boxes

with open("Day5\Movements.txt") as f:
    movements = [[int(s) for s in line.split() if s.isdigit()] for line in f.read().split("\n")]
    for movement in movements:
        move_boxes(boxes_one, movement[0], movement[1] - 1, movement[2] - 1, True)
        move_boxes(boxes_two, movement[0], movement[1] - 1, movement[2] - 1, False)

print("Answer to Q1: {}".format(get_top_boxes(boxes_one)))
print("Answer to Q2: {}".format(get_top_boxes(boxes_two)))