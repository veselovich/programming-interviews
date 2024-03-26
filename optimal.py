import time

import bintrees


class ClientsCreditsInfo:
    def __init__(self):
        self._offset = 0
        self._client_to_credit = {}
        self._credit_to_clients = bintrees.RBTree()

    def insert(self, client_id, c):
        self.remove(client_id)
        self._client_to_credit[client_id] = c - self._offset
        self._credit_to_clients.setdefault(c - self._offset,
                                           set()).add(client_id)

    def remove(self, client_id):
        credit = self._client_to_credit.get(client_id)
        if credit is not None:
            self._credit_to_clients[credit].remove(client_id)
            if not self._credit_to_clients[credit]:
                del self._credit_to_clients[credit]
            del self._client_to_credit[client_id]
            return True
        return False
    
    def lookup(self, client_id):
        credit = self._client_to_credit.get(client_id)
        return -1 if credit is None else credit + self._offset
    
    def add_all(self, C):
        self._offset += C

    def max(self):
        if not self._credit_to_clients:
            return ''
        clients = self._credit_to_clients.max_item()[1]
        return '' if not clients else next(iter(clients))


def main():
    start_time = time.time()

    #test case
    info = ClientsCreditsInfo()

    for i in range(1, 11):
        info.insert(i, i*10)

    info.add_all(5)

    print(info.remove(1))
    print(info.remove(11))

    print(info.lookup(5))
    print(info.lookup(11))

    print(info.max())

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()