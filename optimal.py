import time
from memory_profiler import profile

# The mapping from digit to corresponding characters.
MAPPING = ('O', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO','PQRS', 'TUV', 'WXYZ')

@profile
def phone_mnemonic(phone_number):
    """
    Compute all possible mnemonics for a number
    
    :type phone_number: str
    :rtype: List[str]
    """
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            # All digits are processed, so add partial_mnemonic to mnemonics.
            # (We add a copy since subsequent calls modify partial_mnemonic.)
            mnemonics.append(''.join(partial_mnemonic))
        else:
            # Try all possible characters for this digit.
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)
    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics


def main():
    start_time = time.time()

    #test case
    print(phone_mnemonic("2276696"))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()