import time
from memory_profiler import profile


@profile
def replace_and_remove(size, s):
    """
    Removes all 'b' from array and replace 'a' to 'd', 'd'
    Example
    
    :type size: int
    :type s: list
    :rtype: int
    """
    # Forward iteration: remove 'b's and count the number of 'a's.

    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    # Backward iteration: replace 'a's with 'dd's starting from the end.
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1: write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


def main():
    start_time = time.time()

    #test case
    arr = ['a','c','d','b','b','c','a']
    print(f := replace_and_remove(6, arr))
    print(arr[:f])

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()