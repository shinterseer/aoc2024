import unittest
import numpy as np


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


def turn_right(direction):
    return np.array([[0, 1], [-1, 0]]).dot(direction)


def move_guard(pos, direction, chars):
    direction_to_vector = {
        0: np.array([-1, 0]),  # up
        1: np.array([0, 1]),  # right
        2: np.array([1, 0]),  # down
        3: np.array([0, -1])  # left
    }
    dir_vector = direction_to_vector[direction]
    new_pos = pos + dir_vector
    if new_pos[0] < 0 or new_pos[0] >= chars.shape[0]:
        return np.array([-1, -1]), direction
    if new_pos[1] < 0 or new_pos[1] >= chars.shape[1]:
        return np.array([-1, -1]), direction

    new_direction = direction
    if chars[new_pos[0], new_pos[1]] == '#':
        new_direction = (direction + 1) % 4
        dir_vector = direction_to_vector[new_direction]
        new_pos = pos + dir_vector
    return new_pos, new_direction


def part1_script(input_file):
    chars, pos = get_input(input_file)
    chars[pos[0], pos[1]] = 'X'
    direction = 0
    in_map = True
    while in_map:
        pos, direction = move_guard(pos, direction, chars)
        if pos[0] == -1:
            in_map = False
        else:
            chars[pos[0], pos[1]] = 'X'
    result = len([1 for iy, ix in np.ndindex(chars.shape) if chars[iy, ix] == 'X'])
    return result


def guard_trip(chars, pos):
    directions_dict = {
        0: chars.copy(),  # up
        1: chars.copy(),  # right
        2: chars.copy(),  # down
        3: chars.copy()  # left
    }
    chars[pos[0], pos[1]] = 'X'

    direction = 0

    chars[pos[0], pos[1]] = 'X'

    # in_map = True
    leave = False
    loop = False
    while not leave:
        directions_dict[direction][pos[0], pos[1]] = 'X'
        pos, direction = move_guard(pos, direction, chars)
        # directions_dict[direction][pos[0], pos[1]] = 'X'
        if directions_dict[direction][pos[0], pos[1]] == 'X': # were in a loop
            loop = True
            break

        # directions_dict[direction][pos[0], pos[1]] = 'X'
        if pos[0] == -1:
            # in_map = False
            leave = True
            break
        chars[pos[0], pos[1]] = 'X'

    return chars, leave, loop


def part2_script(input_file):
    chars_original, pos = get_input(input_file)
    x=0
    leave_list = list()
    loop_list = list()
    chars = chars_original.copy()
    print(f'total workload: {chars.shape[0] * chars.shape[1]}')
    for i, j in np.ndindex(chars.shape):
        if i + j % 100 == 0:
            print(f'tested {i + j}')
        chars = chars_original.copy()
        chars[i, j] = '#'
        chars_mod, leave, loop = guard_trip(chars.copy(), pos)
        if leave:
            leave_list.append((i, j))
        if loop:
            loop_list.append((i, j))

    result = len(loop_list)
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    # filename_global = '06_input.txt'
    filename_global = '06_testinput.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
