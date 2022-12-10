commands  = [[c for c in line.split(" ")] for line in open("Day10\Data.txt").read().split("\n")]
X = 1
current_cycle = 1
horizontal_length = 40
vertical_length = 6
x_values = list()

for command in commands:
    x_values.append(X)
    current_cycle += 1
    
    if(command[0]) == "addx":
        x_values.append(X)
        current_cycle += 1
        X += int(command[1])

crt_frame = ""
for j in range(vertical_length):
    for i in range(horizontal_length):
        x_value = x_values[i + (j * horizontal_length)]
        if abs(i - x_value) <= 1:
            crt_frame += "##"
        else:
            crt_frame += "  "
    crt_frame += "\n"

q_one_signals = [20, 60, 100, 140, 180, 220]
print("Answer to Q1: {}".format(sum(map(lambda x: int(x_values[x - 1] * x), q_one_signals))))
print("Answer to Q2:")
print(crt_frame)