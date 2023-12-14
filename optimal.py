import time
from memory_profiler import profile


@profile
def reverse_words(s):
    """
    Reverse words in string
    
    :type s: bytearray
    :rtype: None
    """
    # Assume s is a string encoded as bytearray.
    # First, reverse the whole string.
    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break

        # Reverses each word in the string.
        reverse_range(s, start, end - 1)
        start = end + 1
    # Reverses the last word.
    reverse_range (s, start, len(s) - 1)


def main():
    start_time = time.time()

    #test case
    s = bytearray("Alice likes Bob", 'utf-8')
    reverse_words(s)
    print(s)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()