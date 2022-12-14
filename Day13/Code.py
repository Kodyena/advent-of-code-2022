import ast
from functools import cmp_to_key, reduce
def are_packets_ordered(left, right):
    if(isinstance(left, int) and isinstance(right, int)): return left - right
    if(not isinstance(left, list)): left = [left]
    if(not isinstance(right, list)): right = [right]
    for(a, b) in zip(left, right):
        if (result:=are_packets_ordered(a, b)) != 0: return result
    return len(left) - len(right)

with open("Day13\Data.txt") as f:
    packets = [[ast.literal_eval(line)] for line in f.read().split("\n") if line != ""]


print("Answer to Q1: {}".format(sum(i for i, (left, right) in enumerate(zip(packets[::2], packets[1::2]), start=1) if are_packets_ordered(left, right) < 0)))

dividers = [[[2]], [[6]]]
ordered_packets = sorted(packets + dividers, key=cmp_to_key(are_packets_ordered))
divider_indices = [i for i, x in enumerate(ordered_packets, start=1) if x in dividers]
print("Answer to Q2: {}".format(reduce(lambda x, y: x * y, divider_indices)))