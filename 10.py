import unittest
import numpy as np
import time


class TestExample(unittest.TestCase):
    filename = '10_testinput.txt'

    def test_part1(self):
        self.assertEqual(36, part1_script(self.filename))

    # def test_part2(self):
    #     self.assertEqual(2858, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    array2d = np.array([[int(item) for item in list(line)] for line in lines])

    return array2d


def part1_script(input_file):
    hmap = get_input(input_file)
    result = 0
    return result


def part2_script(input_file):
    hmap = get_input(input_file)
    result = 0
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '09_input.txt'
    # filename_global = '09_testinput.txt'

    start_time = time.time()
    print('part 1 result: ', end='', flush=True)
    result1 = part1_script(filename_global)
    print(result1, end='')
    print(f', time: {time.time() - start_time:.2f} sec')

    start_time = time.time()
    print('part 2 result: ', end='', flush=True)
    result2 = part2_script(filename_global)
    print(result2, end='')
    print(f', time: {time.time() - start_time:.2f} sec')
