import unittest
import numpy as np
import time


class TestExample(unittest.TestCase):
    filename = '08_testinput.txt'

    def test_part1(self):
        self.assertEqual(14, part1_script(self.filename))

    def test_part2(self):
        self.assertEqual(34, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    chars = np.array([list(line) for line in lines])

    return chars


def part1_script(input_file):
    chars = get_input(input_file)
    anti_nodes = np.zeros(chars.shape)
    for i in range(chars.shape[0]):
        for j in range(chars.shape[1]):
            frequency = -1
            if chars[i, j] != '.':
                frequency = chars[i, j]
                for k in range(chars.shape[0]):
                    for l in range(chars.shape[1]):
                        if chars[k][l] == frequency:
                            if i != k or j != l:
                                if 2 * i - k in range(chars.shape[0]) and 2 * j - l in range(chars.shape[1]):
                                    anti_nodes[2 * i - k][2 * j - l] = 1
                                if 2 * k - i in range(chars.shape[0]) and 2 * l - j in range(chars.shape[1]):
                                    anti_nodes[2 * k - i][2 * l - j] = 1

    return anti_nodes.sum()


def part2_script(input_file):
    chars = get_input(input_file)
    anti_nodes = np.zeros(chars.shape)
    for i in range(chars.shape[0]):
        for j in range(chars.shape[1]):
            frequency = -1
            if chars[i, j] != '.':
                frequency = chars[i, j]
                for k in range(chars.shape[0]):
                    for l in range(chars.shape[1]):
                        if chars[k][l] == frequency and (i != k or j != l):
                            m = 0
                            while k + m * (k - i) in range(chars.shape[0]) and l + m * (l - j) in range(chars.shape[1]):
                                anti_nodes[k + m * (k - i)][l + m * (l - j)] = 1
                                m += 1
                            m = 0
                            while i - m * (i - k) in range(chars.shape[0]) and j - m * (j - l) in range(chars.shape[1]):
                                anti_nodes[i - m * (i - k)][j - m * (j - l)] = 1
                                m += 1
    return anti_nodes.sum()


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '08_input.txt'
    # filename_global = '08_testinput.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
