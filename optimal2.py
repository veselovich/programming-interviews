import collections
import time
from memory_profiler import profile

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

@profile
def find_smallest_subarray_covering_subset(stream, query_strings):
    class DoublyLinkedListNode:
        def __init__(self, data=None):
            self.data = data
            self.next = self.prev = None

    class LinkedList:
        def __init__(self):
            self.head = self.tail = None
            self._size = 0

        def __len__(self):
            return self._size
        
        def insert_after(self, value):
            node = DoublyLinkedListNode(value)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1

        def remove(self, node):
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            node.next = node.prev = None
            self._size -= 1

    # Tracks the last occurrence (index) of each string in query-strings.
    loc = LinkedList()
    d = {s: None for s in query_strings}
    result = Subarray(-1, -1)
    for idx, s in enumerate(stream):
        if s in d: #s is in query_strings.
            it = d[s]
            if it is not None:
                # Explicitly removes so that when we add it, it's the string most
                # recently added to loc.
                loc.remove(it)
            loc.insert_after(idx)
            d[s] = loc.tail

            if len(loc) == len(query_strings):
                # We have seen all strings in query_strings, let's get to work.
                if (result== (-1, -1)
                    or idx - loc.head.data < result[1] - result[0]):
                    result = (loc.head.data, idx)
    return result


def main():
    start_time = time.time()

    #test case
    print(find_smallest_subarray_covering_subset(['apple','banana','apple','apple','dog','cat','apple','dog','banana','apple','cat','dog'], {'banana','cat'}))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()