import time
from memory_profiler import profile


@profile
def matrix_search(A, x):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    row, col = 0, len(A[0]) - 1 # Start from the top-right corner.
    # Keeps searching while there are unclassified rows and columns.
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1 # Eliminate this row.
        else: # A[row] [col] > x.
            col -= 1 # Eliminate this column.
    return False


def main():
    start_time = time.time()

    #test case
    matrix = [[-1,2,4,4,6],
              [1,5,5,9,21],
              [3,6,6,9,22],
              [3,6,8,10,24],
              [6,8,9,12,25],
              [8,10,12,13,40]]
    print(matrix_search(matrix, 7))
    print(matrix_search(matrix, 8))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()