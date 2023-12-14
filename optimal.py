import time
from memory_profiler import profile


@profile
def is_palindrome(s):
    """
    Check if string is palindrome
    
    :type s: str
    :rtype: bool
    """
    # i moves forward, and j moves backward.
    i, j = 0, len(s) - 1
    while i < j:
        # i and j both skip non-alphanumeric characters.
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j= i + 1, j - 1
    return True


def main():
    start_time = time.time()

    #test case
    print(is_palindrome("A man, a plan, a canal, Panama"))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()