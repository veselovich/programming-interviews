import collections
import time
from memory_profiler import profile

@profile
def can_form_palindrome(s):
    # A string can be permuted to form a palindrome if and only if the number
    # of chars whose frequencies is odd is at most 1.
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


def main():
    start_time = time.time()

    #test case
    print(can_form_palindrome('edified'))
    print(can_form_palindrome('abcabcdd'))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()