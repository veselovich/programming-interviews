import collections
import time
from memory_profiler import profile


@profile
def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)
    return [
        group for group in sorted_string_to_anagrams.values() if len(group) >= 2
    ]


def main():
    start_time = time.time()

    #test case
    dictionary = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom', 'listen', 'levis', 'money']
    print(find_anagrams(dictionary))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()