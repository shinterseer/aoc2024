import unittest


class TestExample(unittest.TestCase):
    filename = '05_testinput.txt'

    def test_part1(self):
        self.assertEqual(143, part1_script(self.filename))

    def test_part2(self):
        self.assertEqual(123, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    rules = list()
    updates = list()
    current_list = rules
    for line in lines:
        if line == '':
            current_list = updates
            continue
        current_list.append(line)

    rules = [[int(item) for item in rule.split('|')] for rule in rules]
    updates = [[int(item) for item in update.split(',')] for update in updates]
    return rules, updates


def update_correct(update, rules):
    correct = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                correct = False
                break
    return correct


def part1_script(input_file):
    rules, updates = get_input(input_file)
    correct_updates = [update for update in updates if update_correct(update, rules)]
    result = sum([update[int(len(update) / 2)] for update in correct_updates])
    return result


def part2_script(input_file):
    rules, updates = get_input(input_file)
    incorrect_updates = [update for update in updates if not update_correct(update, rules)]

    for update in incorrect_updates:
        swapped = True
        while swapped:
            swapped = False
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    if update.index(rule[0]) > update.index(rule[1]):
                        update[update.index(rule[0])] = rule[1]
                        update[update.index(rule[1])] = rule[0]
                        swapped = True
                        break

    result = sum([update[int(len(update) / 2)] for update in incorrect_updates])
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '05_input.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
