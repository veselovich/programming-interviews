import time
from memory_profiler import profile


@profile
def smallest_nonconstructible_value(A):
    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1:
            break
        max_constructible_value += a
    return max_constructible_value + 1


def main():
    start_time = time.time()

    #test case
    print(smallest_nonconstructible_value([1,1,1,1,1,1,5,10,25]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()