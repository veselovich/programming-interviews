import collections
import time


class QueueWithMax:
    def __init__(self):
        self._entries = collections.deque()
        self._candidates_for_max = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)
        # Eliminate dominated elements in _candidates_for_max.
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)
    
    def dequeue(self) :
        if self._entries:
            result = self._entries.popleft()
            if result == self._candidates_for_max[0] :
                self._candidates_for_max.popleft()
            return result
        raise IndexError('empty queue')
    
    def max(self):
        if self._candidates_for_max:
            return self._candidates_for_max[0]
        raise IndexError('empty queue')


def main():
    start_time = time.time()

    #test case
    queue = QueueWithMax()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.enqueue(2)
    print(queue.max())

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()