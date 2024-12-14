import unittest
import numpy as np
import time


class TestExample(unittest.TestCase):
    filename = '09_testinput.txt'

    def test_part1(self):
        self.assertEqual(1928, part1_script(self.filename))

    def test_part2(self):
        self.assertEqual(2858, part2_script(self.filename))


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
        if expanded_map[i] == '.':
            continue
        else:
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
    def move_last_file(exm, start_looking):
        # get last file - index and num_blocks
        file_index = -1
        file_position_from_end = -1
        for i in range(len(exm)):
            if exm[-1 - start_looking - i] != '.':
                file_position_from_end = start_looking + i
                file_index = exm[-1 - start_looking - i]
                if file_index == '0':
                    return True, file_position_from_end, 0
                break
        num_blocks = 0
        for i in range(len(exm)):
            if exm[-1 - file_position_from_end - i] == file_index:
                num_blocks += 1
            else:
                break
        # find free space of num_blocks and move file there
        empty_blocks = -1
        empty_index = -1
        file_moved = False
        for i in range(len(exm) - file_position_from_end):
            if exm[i] == '.':
                empty_index = i
                empty_blocks = 1
                for j in range(1, len(exm) - i):
                    if exm[i + j] == '.':
                        empty_blocks += 1
                    else:
                        break
                if empty_blocks >= num_blocks:
                    for k in range(num_blocks):
                        exm[empty_index + k] = file_index
                    file_moved = True
                    break

        # remove file from end
        if file_moved:
            for i in range(num_blocks):
                exm[-1 - file_position_from_end - i] = '.'
        return False, file_position_from_end, num_blocks

    disk_map = get_input(input_file)
    expanded_map = get_expanded_map(disk_map)
    f_pos = 0
    n_blocks = 0
    calls = 0
    while True:
        done, f_pos, n_blocks = move_last_file(expanded_map, f_pos + n_blocks)
        calls += 1
        if done:
            break
    result = get_checksum(expanded_map)
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
