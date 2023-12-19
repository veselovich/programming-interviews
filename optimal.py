import time
from memory_profiler import profile


@profile
def get_valid_ip_address(s) :
    """
    Compute all possible valid ip addresses from a string without dot separation
    
    :type s: str
    :rtype: list
    """
    def is_valid_part(s):
        # '00', '000', '01', etc. are not valid, but 'O' is valid.
        return len(s) == 1 or (s[0] != 'O' and int(s) <= 255)
    
    result, parts = [], [None] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                    for k in range (1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i + j:i + j + k], s[i + j + k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
    return result


def main():
    start_time = time.time()

    #test case
    ip = "1921681201"
    print(get_valid_ip_address(ip))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()