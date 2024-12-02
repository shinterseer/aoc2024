import unittest


class TestExample(unittest.TestCase):
    filename = '02_testinput.txt'

    def test_part1(self):
        self.assertEqual(2, part1_script(self.filename))

    def test_part2(self):
        self.assertEqual(4, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    reports = list()
    # reports = [lines[i].split(' ') for i in range(len(lines))]
    for line in lines:
        temp = line.split(' ')
        report = [int(temp[i]) for i in range(len(temp))]
        reports.append(report)
    return reports


def check_safe(rep):
    safe = True
    rcopy = rep.copy()
    rcopy.sort()
    if rep != rcopy:
        rcopy.sort(reverse=True)
        if rep != rcopy:
            safe = False

    for i in range(1, len(rep)):
        if abs(rep[i] - rep[i - 1]) < 1:
            safe = False
        if abs(rep[i] - rep[i - 1]) > 3:
            safe = False
    return safe


def part1_script(input_file):
    reports = get_input(input_file)
    num_safe = 0
    for report in reports:
        if check_safe(report):
            num_safe += 1
    return num_safe


def part2_script(input_file):
    reports = get_input(input_file)
    num_safe = 0
    for report in reports:
        for i in range(len(report)):
            rep = report.copy()
            rep.pop(i)
            if check_safe(rep):
                num_safe += 1
                break
    return num_safe


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '02_input.txt'
    print(f'result 1: {part1_script(filename_global)}')
    print(f'result 2: {part2_script(filename_global)}')
