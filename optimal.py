import functools
import string
import time


def int_to_string(x):
    """
    Converts integer to string
        
    :type x: int
    :rtype: str
    """
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int (s):
    """
    Converts string to integer
        
    :type s: str
    :rtype: int
    """
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


def main():
    start_time = time.time()

    #test case
    print(int_to_string(-123))
    print(string_to_int("-456"))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()