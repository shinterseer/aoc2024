import unittest
import numpy as np

# class TestExample(unittest.TestCase):
#     filename1 = '03_testinput1.txt'
#     filename2 = '03_testinput2.txt'
#
#     def test_part1(self):
#         self.assertEqual(161, part1_script(self.filename1))
#
#     def test_part2(self):
#         self.assertEqual(48, part2_script(self.filename2))


def get_input(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    dim1 = len(lines[0])
    dim2 = len(lines)
    ar = np.array(lines)
    # dia1 = list()
    # for i in range(dim1):
    #     dia1.append([lines[dim1 - i][] ])
    # tester = [[11, 12, 13],
    #           [21, 22, 23],
    #           [31, 32, 33]]
    # tarray = np.array(tester)
    # tarrayf = np.fliplr(tarray)
    # tarrayt = np.transpose(tarray)
    return ar


def part1_script(input_file):
    # count 'XMAS' in lines columns and diagonals forward and backward
    chars = get_input(input_file)
    num_rows = chars.shape[0]
    num_cols = chars.shape[1]
    result = 0
    for i in range(num_rows):
        result += ''.join(chars[i, :]).count("XMAS")
        result += ''.join(chars[i, :]).count("SAMX")
    for i in range(num_cols):
        result += ''.join(chars[:, i]).count("XMAS")
        result += ''.join(chars[:, i]).count("SAMX")



    x=0
    return result


# def part2_script(input_file):
#     input_string = get_input(input_file)
#     input_string = 'do()' + input_string
#
#     current_string = input_string
#     result = 0
#     while len(current_string) > 1:
#         current_string = current_string[current_string.find('do()'):]
#         p2 = current_string.find("don't()")
#         result += process_string(current_string[:p2])
#         current_string = current_string[p2:]
#     return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '04_testinput.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    # result2 = part2_script(filename_global)
    # print(f'result 2: {result2}')
