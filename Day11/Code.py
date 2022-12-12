import re
import operator
import copy
from math import lcm

class Monkey:

    _lowest_common_mul: int = None

    def __init__(self, name, starting_items, operation, test_val, true_monkey = None, false_monkey = None, worry_divider = 3):
        self._name = name
        self._test_val = test_val
        self._operation = operation
        self._items = starting_items
        self._true_monkey = true_monkey
        self._false_monkey = false_monkey
        self._items_inspected = 0
        self._worry_divider = worry_divider
    def __repr__(self) -> str:
        return "Monkey: {}".format(self._name)
    def __str__(self) -> str:
        return self.__repr__()
    def apply_operation(self, item):
        if self._operation[1] != "old":
            return ops[self._operation[0]](item, self._operation[1])
        else:
            return ops[self._operation[0]](item, item)
    def throw_items(self):
        for item in self._items:
            if(self._worry_divider != 1):
                item = self.apply_operation(item) // self._worry_divider
            else:
                item = self.apply_operation(item) % self._lowest_common_mul
            self._items_inspected += 1
            if(item % self._test_val == 0):
                self._true_monkey._items.append(item)
            else:
                self._false_monkey._items.append(item)
        self._items = list()

monkeys = list()
ops = {'+' : operator.add, '*' : operator.mul}
number_of_rounds_1 = 20
number_of_rounds_2 = 10000

with open("Day11\Data.txt") as f:
    for monkey_data in f.read().split("\n\n"):
        digits = [[int(s) for s in re.findall('[0-9]+', line) ] for line in monkey_data.split("\n")]
        op = re.findall(r'[*|\+]', monkey_data)[0]
        operation = list([op])
        if(len(digits[2])) == 0: operation.append("old")
        else: operation.append(digits[2][0])
        monkeys.append(Monkey(digits[0][0], list(digits[1]), operation, digits[3][0], digits[4][0], digits[5][0]))

monkeys.sort(key=lambda x: x._name)

for monkey in monkeys:
    monkey._true_monkey = monkeys[monkey._true_monkey]
    monkey._false_monkey = monkeys[monkey._false_monkey]

monkeys_2 = copy.deepcopy(monkeys)

for i in range(number_of_rounds_1):
    for monkey in monkeys:
        monkey.throw_items()

lowest_common_mul = lcm(*[m._test_val for m in monkeys_2])

for monkey in monkeys_2:
    monkey._worry_divider = 1
    monkey._lowest_common_mul = lowest_common_mul

for i in range(number_of_rounds_2):
    for monkey in monkeys_2:
        monkey.throw_items()

items_inspected_1 = [monkey._items_inspected for monkey in monkeys]
items_inspected_1.sort()
items_inspected_1.reverse()
print("Answer to Q1: {}".format(items_inspected_1[0] * items_inspected_1[1]))

items_inspected_2 = [monkey._items_inspected for monkey in monkeys_2]
items_inspected_2.sort()
items_inspected_2.reverse()
print("Answer to Q2: {}".format(items_inspected_2[0] * items_inspected_2[1]))