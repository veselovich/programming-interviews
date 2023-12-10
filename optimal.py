import time
from memory_profiler import profile

class RotatedMatrix:
    def __init__(self, square_matrix):
        self._square_matrix = square_matrix

    def read_entry(self, i, j):
    # Note that A[~i] for i in [0, len(A) - 1] is A[~(i + 1)].
        return self._square_matrix[~j][i]
    
    def write_entry(self, i, j, v):
        self._square_matrix[~j][i] = v

@profile
def rotate_matrix(square_matrix):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # Perform a 4-way exchange. Note that A[~i] for i in [0, len(A) - 1]
            # is A[-(i + 1)].
            (square_matrix[i][j],
             square_matrix[~j][i],
             square_matrix[~i][~j],
             square_matrix[j][~i]) = (square_matrix[~j][i],
                                     square_matrix[~i][~j],
                                     square_matrix[j][~i],
                                     square_matrix[i][j])


def main():
    start_time = time.time()

    #test case
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]

    rotate_matrix(matrix)
    print(matrix)

    # rotate again (initial matrix is upside down)
    m = RotatedMatrix(matrix)
    print(m.read_entry(0, 0))
    
    m.write_entry(0, 0, 17)
    print(m.read_entry(0, 0))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()