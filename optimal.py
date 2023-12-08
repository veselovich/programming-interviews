import time
import math
import collections
from memory_profiler import profile


@profile
def is_valid_sudoku(partial_assignment):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    # Return True if subarray
    # partial_assignment [start_row: end_row] [start_col: end_col] contains any
    # duplicates in {1, 2, ..., len(partial_assignment)}; otherwise
    # False.
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))
    
    n = len(partial_assignment)
    # Check row and column constraints.
    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False
    
    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))

# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(
        collections.Counter(k
                            for i, row in enumerate(partial_assignment)
                            for j, c in enumerate(row)
                            if c!= 0
                            for k in ((i, str(c)),
                                      (str(c), j),
                                      (i / region_size, j / region_size, str(c))
                                      )).values(),
                                       default=0) <= 1

def main():
    start_time = time.time()

    #test case
    sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

    print(is_valid_sudoku(sudoku_board))
    print(is_valid_sudoku_pythonic(sudoku_board))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()