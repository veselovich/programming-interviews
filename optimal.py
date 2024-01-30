import time
from memory_profiler import profile


class Queue:
    def __init__(self):
        self._enq, self._deq = [], []

    def enqueue(self, x):
        self._enq.append(x)

    def dequeue (self):
        if not self._deq:
            # Transfers the elements in _enq to _deq.
            while self._enq:
                self._deq.append(self._enq.pop())
        if not self._deq: #_deq is still empty!
            raise IndexError ('empty queue')
        return self._deq.pop()


def main():
    start_time = time.time()

    #test case
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()