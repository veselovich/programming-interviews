import itertools
import time


def look_and_say(n):
    """
    Genereate sequence of digits, pronouncing previous sequence
    
    :type n: int
    :rtype: List[int]
    """
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)

    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s

# Pythonic solution uses the power of itertools.groupby().
def look_and_say_pythonic(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s


def main():
    start_time = time.time()

    #test case

    print(look_and_say(8))
    print(look_and_say_pythonic(8))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()