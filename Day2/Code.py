char_to_val = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def result(x, y):
    return (1 + (y - x)) % 3 * 3

def getChoice(x, y):
    return (y - 3 + x) % 3 + 1

with open("Day2\Data\Guide.txt") as f:
    results = [[char_to_val[c] for c in line.split(" ")] for line in f.read().split("\n")]
    score_game_one = sum((map(lambda x: result(x[0], x[1]) + x[1], results)))
    score_game_two = sum((map(lambda x: result(x[0], getChoice(x[0], x[1])) + getChoice(x[0], x[1]), results)))

print("Score game 1: {}".format(score_game_one))
print("Score game 2: {}".format(score_game_two)) 