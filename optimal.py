import time
from memory_profiler import profile

import collections
Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

@profile
def intersect_rectangle (R1, R2):
    """
    Check if rectangles intersect, given start vertex of rectangles and their dimensions
    
    :type R1, R1: Rectangle
    :rtype: Rectangle
    """
    def is_intersect (R1, R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)
    
    if not is_intersect (R1, R2):
        return Rectangle(0, 0, -1, -1) # No intersection.
    return Rectangle(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))


def main():
    start_time = time.time()

    #test case
    R1 = Rectangle(0, 0, 3, 3)
    R2 = Rectangle(1, 1, 4, 4)
    print(intersect_rectangle(R1, R2))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()