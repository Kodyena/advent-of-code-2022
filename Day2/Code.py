outcomes = {
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "A X": 4,
    "B Y": 5,
    "C Z": 6
}

outcomesTwo = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

with open("Day2\Data\Guide.txt") as f:
    results = f.read().split("\n")
    print("Score: {}".format(sum(map(lambda l: outcomesTwo[l], results))))