import unittest


# import numpy as np


class TestExample(unittest.TestCase):
    filename = '05_testinput.txt'

    def test_part1(self):
        self.assertEqual(143, part1_script(self.filename))

    # def test_part2(self):
    #     self.assertEqual(9, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    rules = list()
    updates = list()
    part2 = False
    for line in lines:
        if line == '':
            part2 = True
            continue
        if part2:
            updates.append(line)
        else:
            rules.append(line)

    rules = [[int(item) for item in rule.split('|')] for rule in rules]
    updates = [[int(item) for item in update.split(',')] for update in updates]
    return rules, updates


def part1_script(input_file):
    rules, updates = get_input(input_file)
    correct_updates = list()

    for update in updates:
        is_ok = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    is_ok = False
        if is_ok:
            correct_updates.append(update)

    result = 0
    for update in correct_updates:
        result += update[int(len(update) / 2)]

    return result


# def part2_script(input_file):
#     return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '05_input.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    # result2 = part2_script(filename_global)
    # print(f'result 2: {result2}')
