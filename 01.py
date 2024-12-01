import unittest


class TestExample(unittest.TestCase):
    filename = '01_testinput.txt'

    def test_part1(self):
        self.assertEqual(11, part1_script(self.filename))

    def test_part2(self):
        self.assertEqual(31, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    numbers1 = [int(lines[k].split(' ')[0]) for k in range(len(lines))]
    numbers2 = [int(lines[k].split(' ')[-1]) for k in range(len(lines))]
    return numbers1, numbers2


def part1_script(input_file):
    numbers1, numbers2 = get_input(input_file)
    numbers1.sort()
    numbers2.sort()
    result = sum([abs(numbers2[i] - numbers1[i]) for i in range(len(numbers2))])
    return result


def part2_script(input_file):
    numbers1, numbers2 = get_input(input_file)
    result = 0
    for i in range(len(numbers1)):
        result += numbers1[i] * numbers2.count(numbers1[i])
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename = '01_input1.txt'
    print(f'result 1: {part1_script(filename)}')
    print(f'result 2: {part2_script(filename)}')
