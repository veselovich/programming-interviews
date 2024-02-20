import heapq
import math
from random import randint
import time
from memory_profiler import profile


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __lt__(self, rhs):
        return self.distance < rhs.distance
    
    def __repr__(self) -> str:
        return f'Star {self.x, self.y, self.z}'


def find_closest_k_stars(stars, k):
    # max_heap to store the closest k stars seen so far.
    max_heap = []
    for star in stars:
        # Add each star to the max-heap. If the max-heap size exceeds k, remove
        # the maximum element from the max-heap.
        # As python has only min-heap, insert tuple (negative of distance, star)
        # to sort in reversed distance order.
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    # Iteratively extract from the max-heap, which yields the stars sorted
    # according from furthest to closest.
    return [s[1] for s in heapq.nlargest(k, max_heap)]


def main():
    start_time = time.time()

    #test case
    stars = []
    for _ in range(20):
        s = Star(randint(1,1000), randint(1,1000), randint(1,1000))
        print(s)
        stars.append(s)

    print('\nClosest:')
    for s in find_closest_k_stars(stars, k=3):
        print(s)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()