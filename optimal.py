import time
from memory_profiler import profile


@profile
def is_palindromic(s):
    """
    Check if string is palindromic
    Example: "abcba" - True
    
    :type s: str
    :rtype: bool
    """
    return all(s[i] == s[~i] for i in range(len(s) // 2))


def main():
    start_time = time.time()

    #test case
    print(is_palindromic("abcba"))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()