def char_to_priorty_val(c):
    return int(ord(c)) - (38 if c <= 'Z' else 96)

with open("Day3\Data\Data.txt") as f:
    lines = [line for line in f.read().split("\n")]
    intersections = [[c for c in set(line[:len(line)//2]).intersection(line[len(line)//2:]) if c != ' '] for line in lines ]
    intersections = [i for j in intersections for i in j]
    groups = [lines[i * 3:(i + 1) * 3] for i in range((len(lines) + 2) // 3)]
    groupIntersections = [set.intersection(*map(lambda s: set(s), group)).pop() for group in groups]

    print("Answer to Q1: {}".format(sum(map(lambda x: char_to_priorty_val(x), intersections))))
    print("Answer to Q2: {}".format(sum(map(lambda x: char_to_priorty_val(x), groupIntersections))))


