import time
from memory_profiler import profile


@profile
def snake_string(s) :
    """
    Write given string in snake order
    
    :type s: str
    :rtype: str
    """
    result = []
    # Outputs the first row, i.e., s[1], s[5], s[9],
    for i in range(1, len(s), 4):
        result.append(s[i])
    # Outputs the second row, i.e., s[0], s[2], s[4],
    for i in range(0, len(s), 2):
        result.append(s[i])
    # Outputs the third row, i.e., s[3], s[7], s[11],
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)

# Python solution uses slicing with right steps.
def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]


def main():
    start_time = time.time()

    #test case
    print(snake_string("Hello World"))
    print(snake_string_pythonic("Hello World"))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()