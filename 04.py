import unittest
import numpy as np


class TestExample(unittest.TestCase):
    filename = '04_testinput.txt'

    def test_part1(self):
        self.assertEqual(18, part1_script(self.filename))

    def test_part2(self):
        self.assertEqual(9, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    ar = np.array(lines)
    return ar


def part1_script(input_file):
    def count_occurance(charlist, str1='XMAS', str2='SAMX'):
        count = 0
        count += ''.join(charlist).count(str1)
        count += ''.join(charlist).count(str2)
        return count

    chars = get_input(input_file)
    charsf = np.fliplr(chars)
    num_rows = chars.shape[0]
    num_cols = chars.shape[1]
    result = 0
    for i in range(num_rows):
        result += count_occurance(chars[i, :])
    for i in range(num_cols):
        result += count_occurance(chars[:, i])

    result += count_occurance(np.diagonal(chars))
    for i in range(1, num_rows):  # diagonals
        result += count_occurance(np.diagonal(chars, offset=i))
        result += count_occurance(np.diagonal(chars, offset=-i))

    result += count_occurance(np.diagonal(charsf))
    for i in range(1, num_rows):  # diagonals
        result += count_occurance(np.diagonal(charsf, offset=i))
        result += count_occurance(np.diagonal(charsf, offset=-i))
    return result


def part2_script(input_file):
    chars = get_input(input_file)
    result = 0
    for i in range(1, chars.shape[0] - 1):
        for j in range(1, chars.shape[1] - 1):
            if chars[i, j] == 'A':
                if ((chars[i - 1, j - 1] == 'M' and chars[i + 1, j + 1] == 'S') or
                        (chars[i - 1, j - 1] == 'S' and chars[i + 1, j + 1] == 'M')):
                    if ((chars[i + 1, j - 1] == 'M' and chars[i - 1, j + 1] == 'S') or
                            (chars[i + 1, j - 1] == 'S' and chars[i - 1, j + 1] == 'M')):
                        result += 1
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '04_input.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
