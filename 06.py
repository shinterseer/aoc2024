import unittest
import numpy as np
import time


class TestExample(unittest.TestCase):
    filename = '06_testinput.txt'

    def test_part1(self):
        self.assertEqual(41, part1_script(self.filename))

    def test_part2(self):
        self.assertEqual(6, part2_script(self.filename))


def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    chars = np.array([list(line) for line in lines])
    pos = None
    for i in range(chars.shape[0]):
        for j in range(chars.shape[1]):
            if chars[i, j] == '^':
                pos = np.array([i, j])
    return chars, pos


def move_guard(pos, direction, chars):
    direction_to_vector = {
        0: np.array([-1, 0]),  # up
        1: np.array([0, 1]),  # right
        2: np.array([1, 0]),  # down
        3: np.array([0, -1])  # left
    }
    while True:
        dir_vector = direction_to_vector[direction]
        new_pos = pos + dir_vector

        if new_pos[0] < 0 or new_pos[0] >= chars.shape[0]:
            return np.array([-1, -1]), direction
        if new_pos[1] < 0 or new_pos[1] >= chars.shape[1]:
            return np.array([-1, -1]), direction

        if chars[new_pos[0], new_pos[1]] != '#':
            new_pos = pos + dir_vector
            return new_pos, direction
        else:
            direction = (direction + 1) % 4


def guard_trip(chars, pos):
    directions_dict = {
        0: chars.copy(),  # up
        1: chars.copy(),  # right
        2: chars.copy(),  # down
        3: chars.copy()  # left
    }

    direction = 0
    chars[pos[0], pos[1]] = 'X'

    leave = False
    loop = False
    while not leave:
        old_pos = pos.copy()
        pos, direction = move_guard(pos, direction, chars)
        # directions_dict[direction][pos[0], pos[1]] = 'X'
        if directions_dict[direction][old_pos[0], old_pos[1]] == 'X':  # were in a loop
            loop = True
            break

        if pos[0] == -1:
            leave = True
            break
        directions_dict[direction][old_pos[0], old_pos[1]] = 'X'
        chars[pos[0], pos[1]] = 'X'

    return chars, leave, loop


def part1_script(input_file):
    chars, pos = get_input(input_file)
    chars, leave, loop = guard_trip(chars, pos)
    result = len([1 for iy, ix in np.ndindex(chars.shape) if chars[iy, ix] == 'X'])
    return result


def part2_script(input_file):
    chars_original, pos = get_input(input_file)
    leave_list = list()
    loop_list = list()
    chars = chars_original.copy()
    start_time = time.time()
    print(f'total rows: {chars.shape[0]}')
    for i in range(chars.shape[0]):
        print(f'row: {i}, loops found: {len(loop_list)}', flush=True)
        for j in range(chars.shape[1]):
            chars = chars_original.copy()
            chars[i, j] = '#'
            chars_mod, leave, loop = guard_trip(chars.copy(), pos)
            if leave:
                leave_list.append((i, j))
            if loop:
                loop_list.append((i, j))
    print(f'total time for part 2 in s: {time.time() - start_time:.2f}')
    result = len(loop_list)
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '06_input.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
