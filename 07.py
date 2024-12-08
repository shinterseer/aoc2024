import unittest
import numpy as np
import time


# class TestExample(unittest.TestCase):
#     filename = '07_testinput.txt'
#
#     def test_part1(self):
#         self.assertEqual(41, part1_script(self.filename))
#
#     def test_part2(self):
#         self.assertEqual(6, part2_script(self.filename))

def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    proc1 = [line.split(':') for line in lines]
    equations = [[int(s) for s in proc[1].split(' ')[1:]] for proc in proc1]
    test_values = [int(proc[0]) for proc in proc1]

    return test_values, equations



def part1_script(input_file):
    test_values, equations = get_input(input_file)
    result = 0
    for i in range(len(test_values)):
        num_operations = len(equations[i]) - 1
        equation = equations[i]
        test_value = test_values[i]
        for j in range(2 ** num_operations):
            operations = list(format(j, f'#0{num_operations + 2}b'))[2:]
            test_result = equation[0]
            for k in range(len(operations)):
                if operations[k] == '0':
                    test_result += equation[k + 1]
                if operations[k] == '1':
                    test_result *= equation[k + 1]
            if test_result == test_value:
                # found = True
                # found_at = j
                result += test_value
                break
    return result

#
# def part2_script(input_file):
#     chars_original, pos = get_input(input_file)
#     leave_list = list()
#     loop_list = list()
#     chars = chars_original.copy()
#     start_time = time.time()
#     print(f'total rows: {chars.shape[0]}')
#     for i in range(chars.shape[0]):
#         print(f'row: {i}, loops found: {len(loop_list)}', flush=True)
#         for j in range(chars.shape[1]):
#             chars = chars_original.copy()
#             chars[i, j] = '#'
#             chars_mod, leave, loop = guard_trip(chars.copy(), pos)
#             if leave:
#                 leave_list.append((i, j))
#             if loop:
#                 loop_list.append((i, j))
#     print(f'total time for part 2 in s: {time.time() - start_time:.2f}')
#     result = len(loop_list)
#     return result


if __name__ == '__main__':
    unittest.main(exit=False)

    filename_global = '07_input.txt'
    # filename_global = '07_testinput.txt'
    result1 = part1_script(filename_global)
    print(f'result 1: {result1}')
    # result2 = part2_script(filename_global)
    # print(f'result 2: {result2}')15:52

