import unittest
import numpy as np

class TestExample(unittest.TestCase):
    filename = '06_testinput.txt'

    def test_part1(self):
        self.assertEqual(41, part1_script(self.filename))

    # def test_part2(self):
    #     self.assertEqual(123, part2_script(self.filename))


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

def move_guard(pos, text_direction, chars):
    direction = None
    if text_direction == 'up':
        direction = np.array([-1, 0])
    if text_direction == 'down':
        direction = np.array([1, 0])
    if text_direction == 'left':
        direction = np.array([0, -1])
    if text_direction == 'right':
        direction = np.array([0, 1])

    new_pos = pos + direction
    if new_pos[0] < 0 or new_pos[0] >= chars.shape[0]:
        return np.array([-1, -1]), direction
    if new_pos[1] < 0 or new_pos[1] >= chars.shape[1]:
        return np.array([-1, -1]), direction

    new_direction = direction.copy()
    if chars[new_pos[0], new_pos[1]] == '#':
        new_direction = turn_right(direction)
        new_pos = pos + new_direction
    return new_pos, new_direction

def part1_script(input_file):
    chars, pos = get_input(input_file)
    chars[pos[0], pos[1]] = 'X'
    # pos_list = [pos]
    direction = 'up'
    # direction = np.array([-1, 0])
    in_map = True
    while in_map:
        pos, direction = move_guard(pos, direction, chars)
        if pos[0] == -1:
            in_map = False
        else:
            chars[pos[0], pos[1]] = 'X'
    result = len([1 for iy, ix in np.ndindex(chars.shape) if chars[iy, ix] == 'X'])
    return result


def part2_script(input_file):
    chars, pos = get_input(input_file)
    chars[pos[0], pos[1]] = 'X'
    walked_directions_dict = {
        'up': list(),
        'down': list(),
        'left': list(),
        'right': list(),
    }
    # pos_list = [pos]
    direction = np.array([-1, 0])

    in_map = True
    # while in_map:
    #     if direction == np.array([-1, 0]):
    #         walked_directions_dict['up'].append(pos)
    #     if direction == np.array([1, 0]):
    #         walked_directions_dict['down'].append(pos)
    #     if direction == np.array([0, -1]):
    #         walked_directions_dict['left'].append(pos)
    #     if direction == np.array([0, 1]):
    #         walked_directions_dict['right'].append(pos)
    #
    #     pos, direction = move_guard(pos, direction, chars)
    #     if pos[0] == -1:
    #         in_map = False
    #     else:
    #         chars[pos[0], pos[1]] = 'X'



    result = 0
    return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '06_input.txt'
    # filename_global = '06_testinput.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    result2 = part2_script(filename_global)
    print(f'result 2: {result2}')
