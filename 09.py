import unittest
import numpy as np
import time

class TestExample(unittest.TestCase):
    filename = '09_testinput.txt'

    def test_part1(self):
        self.assertEqual(1928, part1_script(self.filename))

    # def test_part2(self):
    #     self.assertEqual(123, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    disk_map = list(lines[0])
    return disk_map


def get_expanded_map(disk_map):
    expanded_map = []
    file_index = 0
    for i in range(int(len(disk_map) / 2)):
        file_blocks = int(disk_map[2 * i])
        free_blocks = int(disk_map[2 * i + 1])
        expanded_map += [str(file_index)] * file_blocks
        expanded_map += ['.'] * free_blocks
        file_index += 1
    if len(disk_map) % 2 != 0:
        expanded_map += [str(file_index)] * int(disk_map[-1])
    return expanded_map




def get_checksum(expanded_map):
    checksum = 0
    for i in range(len(expanded_map)):
        checksum += int(expanded_map[i]) * i
    return checksum

def part1_script(input_file):
    def move_last_block(exm):
        if exm[-1] == '.':
            return exm[:-1]
        file_index = exm[-1]

        for idx in range(len(exm)):
            if exm[idx] == '.':
                exm[idx] = file_index
                break
        return exm[:-1]

    disk_map = get_input(input_file)
    expanded_map = get_expanded_map(disk_map)

    while True:
        expanded_map = move_last_block(expanded_map)
        if not ('.' in expanded_map):
            break

    result = get_checksum(expanded_map)
    return result


def part2_script(input_file):
    disk_map = get_input(input_file)
    return 0


if __name__ == '__main__':
    unittest.main(exit=False)

    # filename_global = '09_input.txt'
    filename_global = '09_testinput.txt'

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
