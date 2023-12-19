import functools
import time
from memory_profiler import profile


@profile
def roman_to_integer(s):
    """
    Converts valid roman integer to decimal
    "LIX" -> 59
    
    :type s: str
    :rtype: int
    """
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        reversed(range(len(s) - 1)), T[s[-1]])


def main():
    start_time = time.time()

    #test case
    roman = "LIX"
    print(roman_to_integer(roman))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()