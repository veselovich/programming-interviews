import time
from memory_profiler import profile


@profile
def matrix_in_spiral_order(square_matrix):
    """
    Returns an array of values from square matrix, ordered in clockwise spiral
    
    :type square_matrix: list
    :rtype: list
    """
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix))
            or next_y not in range(len(square_matrix))
            or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering

def main():
    start_time = time.time()

    #test case
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    
    matrix2 = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]

    print(matrix_in_spiral_order(matrix2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()