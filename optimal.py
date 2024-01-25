import time
from memory_profiler import profile


@profile
def is_well_formed(s):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            # Unmatched right char or mismatched chars.
            return False
    return not left_chars


def main():
    start_time = time.time()

    #test case
    print(is_well_formed('{}{[()][]}'))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()