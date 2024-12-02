import unittest

#
# class TestExample(unittest.TestCase):
#     filename = '01_testinput.txt'
#
#     def test_part1(self):
#         self.assertEqual(11, part1_script(self.filename))
#
#     def test_part2(self):
#         self.assertEqual(31, part2_script(self.filename))
#

def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def part1_script(input_file):
    lines = get_input(input_file)
    reports = list()
    # reports = [lines[i].split(' ') for i in range(len(lines))]
    for line in lines:
        temp = line.split(' ')
        report = [int(temp[i]) for i in range(len(temp))]
        reports.append(report)

    num_safe = 0
    for report in reports:
        rcopy = report.copy()
        rcopy.sort()
        if report == rcopy:
            num_safe += 1
            continue
        rcopy.sort(reverse=True)
        if report == rcopy:
            num_safe += 1
    x = 0

    return num_safe


if __name__ == '__main__':
    unittest.main(exit=False)

    # filename_global = '02_input.txt'
    filename_global = '02_testinput.txt'

    print(f'result 1: {part1_script(filename_global)}')
