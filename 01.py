def get_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    numbers1 = [int(lines[k].split(' ')[0]) for k in range(len(lines))]
    numbers2 = [int(lines[k].split(' ')[-1]) for k in range(len(lines))]
    return numbers1, numbers2


def main_script1():
    numbers1, numbers2 = get_input('01_input1.txt')
    result = sum([abs(numbers2[i] - numbers1[i]) for i in range(len(numbers2))])
    print(f'result 1: {result}')


def main_script2():
    numbers1, numbers2 = get_input('01_input1.txt')
    result = 0
    for i in range(len(numbers1)):
        result += numbers1[i] * numbers2.count(numbers1[i])
    print(f'result 2: {result}')
    print()


if __name__ == '__main__':
    main_script1()
    main_script2()
