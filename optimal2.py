import collections
import time


class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
                                                  ('element', 'max'))
    
    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0
    
    def max(self) :
        if self.empty():
            raise IndexError ('max (): empty stack')
        return self._element_with_cached_max [-1].max
    
    def pop(self) :
        if self.empty():
            raise IndexError ('pop (): empty stack')
        return self._element_with_cached_max.pop().element
    
    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(
                x, self.max())))


class QueueWithMax:
    def __init__(self):
        self._enqueue = Stack()
        self._dequeue = Stack()
    
    def enqueue(self, x):
        self._enqueue.push(x)
    
    def dequeue(self):
        if self._dequeue.empty():
            while not self._enqueue.empty():
                self._dequeue.push(self._enqueue.pop())
        if not self._dequeue.empty():
            return self._dequeue.pop()
        raise IndexError('empty queue')
    
    def max(self):
        if not self._enqueue.empty():
            return self._enqueue.max() if self._dequeue.empty() else max(
                self._enqueue.max(), self._dequeue.max())
        if not self._dequeue.empty():
            return self._dequeue.max()
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