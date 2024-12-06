import unittest
import re


class TestExample(unittest.TestCase):
    filename1 = '03_testinput1.txt'
    filename2 = '03_testinput2.txt'

    def test_part1(self):
        self.assertEqual(161, part1_script(self.filename1))

    def test_part2(self):
        self.assertEqual(48, part2_script(self.filename2))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return ''.join(lines)


def process_string(input_string):
    match = re.findall(r'mul\(\d+,\d+\)', input_string)
    result = 0
    for m in match:
        parts = m.split(',')
        n1 = int(re.search(r'\d+', parts[0]).group())
        n2 = int(re.search(r'\d+', parts[1]).group())
        result += n1 * n2
    return result


def part1_script(input_file):
    input_string = get_input(input_file)
    result = process_string(input_string)
    return result


def part2_script(input_file):
    input_string = get_input(input_file)
    input_string = 'do()' + input_string

    current_string = input_string
    result = 0
    while len(current_string) > 1:
        current_string = current_string[current_string.find('do()'):]
        p2 = current_string.find("don't()")
        result += process_string(current_string[:p2])
        current_string = current_string[p2:]
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '03_input.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
