import functools
import string
import time
from memory_profiler import profile


@profile
def convert_base(num_as_string, b1, b2):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())
    
    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('O' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


def main():
    start_time = time.time()

    #test case
    print(convert_base('255', 10, 16))
    print(convert_base('10', 10, 11))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()