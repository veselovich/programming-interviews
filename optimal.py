import time


class Queue:
    SCALE_FACTOR = 2
    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries): # Needs to resize.
        # Makes the queue elements appear consecutively.
            self._entries = (
                self._entries[self._head:] + self._entries[:self._head])
            # Resets head and tail.
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (
                len (self._entries) * Queue.SCALE_FACTOR - len(self._entries))
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError ('empty queue')
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return ret

    def size(self):
        return self._num_queue_elements


def main():
    start_time = time.time()

    #test case
    queue = Queue(2)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    queue.enqueue(5)
    queue.enqueue(6)
    print(queue.size())


    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()