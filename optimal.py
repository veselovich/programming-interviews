import time
from memory_profiler import profile


@profile
def decoding(s) :
    """
    Run-length-encoding(RLE):
    "aaaabcccaa" -> "4a1b3c2a"
    
    :type s: str
    :rtype: s
    """
    count, result = 0, []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else: # c is a letter of alphabet.
            result.append(c * count) # Appends count copies of c to result.
            count = 0
    return ''.join(result)

def encoding(s):
    result, count = [], 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            # Found new character so write the count of previous character.
            result.append(str(count) + s[i - 1])
            count = 1
        else: # s[i] == s[i - 1].
            count += 1
    return ''.join(result)


def main():
    start_time = time.time()

    #test case
    print(decoding("4a1b3c2a"))
    print(encoding("aaaabcccaa"))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()