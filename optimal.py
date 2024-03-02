import collections
import time
from memory_profiler import profile


class LRUCache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn, price):
        # We add the value for key only if key is not present - we don't update
        # existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None


def main():
    start_time = time.time()

    #test case
    cache = LRUCache(5)
    cache.lookup(1234567890)
    cache.insert(1234567892, 20)
    for i in range(10):
        cache.insert(1234567890+i, (i+1)*10)
    cache.erase(1234567896)
    print(cache.lookup(1234567898))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()