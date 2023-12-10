import time
from memory_profiler import profile


@profile
def matrix_in_spiral_order(square_matrix):
    """
    Returns an array of values from square matrix, ordered in clockwise spiral
    
    :type square_matrix: list
    :rtype: list
    """
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset])
            return
        
        spiral_ordering.extend(square_matrix[offset][offset: -1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset: -1 - offset])
        spiral_ordering.extend(
            square_matrix[-1 - offset][-1 - offset: offset: -1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset: offset: -1])
        
    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise (offset)
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