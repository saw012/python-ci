import sys


def addition(value1, value2):
    if not isinstance(value1, int) and not isinstance(value2, int):
        print('Invalid input')
        return 'Invalid input'
    else:
        print('value1 + value2 = ', value1 + value2)
        return value1 + value2


if __name__ == '__main__':
    print('value1 = ', sys.argv[1], '\nvalue2 = ', sys.argv[2])
    addition(int(sys.argv[1]), int(sys.argv[2]))
