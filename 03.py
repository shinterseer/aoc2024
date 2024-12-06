import unittest
import re



class TestExample(unittest.TestCase):
    filename1 = '03_testinput1.txt'
    filename2 = '03_testinput2.txt'

    def test_part1(self):
        self.assertEqual(161, part1_script(self.filename1))

    # def test_part2(self):
    #     self.assertEqual(4, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines
    # reports = list()
    # # reports = [lines[i].split(' ') for i in range(len(lines))]
    # for line in lines:
    #     temp = line.split(' ')
    #     report = [int(temp[i]) for i in range(len(temp))]
    #     reports.append(report)
    # return reports


#
#
# def check_safe(rep):
#     safe = True
#     rcopy = rep.copy()
#     rcopy.sort()
#     if rep != rcopy:
#         rcopy.sort(reverse=True)
#         if rep != rcopy:
#             safe = False
#
#     for i in range(1, len(rep)):
#         if abs(rep[i] - rep[i - 1]) < 1:
#             safe = False
#         if abs(rep[i] - rep[i - 1]) > 3:
#             safe = False
#     return safe
#

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
    lines = get_input(input_file)
    input_string = ''.join(lines)
    return process_string(input_string)
    # match = re.findall(r'mul\(\d+,\d+\)', input_string)
    # result = 0
    # for m in match:
    #     parts = m.split(',')
    #     n1 = int(re.search(r'\d+', parts[0]).group())
    #     n2 = int(re.search(r'\d+', parts[1]).group())
    #     result += n1 * n2
    # return result


def part2_script(input_file):
    lines = get_input(input_file)
    input_string = ''.join(lines)
    position = 0
    done = False
    while not done:
        p1 = input_string[position:].find('do()') + len('do()')
        p2 = p1 + input_string[p1:].find("don't()") + len("don't()")
        position += p2
    print(input_string[p1:p2])
    return input_string[p1:p2]
    return 0


if __name__ == '__main__':
    unittest.main(exit=False)
    #
    # filename_global = '03_testinput.txt'
    filename_global = '03_input.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
