import time
from memory_profiler import profile


@profile
def multiply(num1, num2):
    """
    Given to numbers as an arrays calculate their product
    Example: [1,2,3] , [9,8,7] -> [1,2,1,4,0,1]
    
    :type num1, num2: list
    :rtype: list
    """
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeroes:
    # get each non-zero-digit index as an iterator
    # next() takes the first element, but if there is no elements by default it returns len()
    # slice from this element to the end. If no elements slice is: [len(list):] = []
    # pick between list or [0](if list is [])
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


def main():
    start_time = time.time()

    #test case
    num1 = [1,2,3]
    num2 = [9,8,7]
    print(multiply(num1, num2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()