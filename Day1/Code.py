import os
f = open(os.path.join(os.path.dirname(__file__),"Data/Calories.txt"))
text = f.read().split(sep="\n\n")
text = [[int(line) for line in sublist.split("\n") if line != ""] for sublist in text]
calories = list(map(sum, text))
calories.sort()

print("Top elf had {} calories".format(calories[-1]))
print("Top three elves had {} calories".format(sum(calories[-3:])))