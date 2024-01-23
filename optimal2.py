import collections
import time
from memory_profiler import profile


class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self. count = max, count


    def __init__(self):
        self._element = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._element) == 0
    
    def max(self):
        if self.empty():
            raise IndexError ('max (): empty stack')
        return self._cached_max_with_count[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError ('pop (): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count == 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element
    
    def push(self, x) :
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x, 1))


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