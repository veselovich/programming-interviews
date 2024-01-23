import collections
import time
from memory_profiler import profile


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


def main():
    start_time = time.time()

    #test case
    stack = Stack()
    stack.push(1)
    stack.push(9)
    stack.push(7)
    stack.push(5)
    
    print(stack.max())

    print(stack.pop())

    print(stack.empty())

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()