datastream = open("Day6\Data.txt").read()

for i in range(0, len(datastream) - 4, 1):
    if(len(set(datastream[i:i+4])) == 4):
        print("Answer to Q1: {}".format(i + 4))
        break

for i in range(0, len(datastream) - 14, 1):
    if(len(set(datastream[i:i+14])) == 14):
        print("Answer to Q2: {}".format(i + 14))
        break

