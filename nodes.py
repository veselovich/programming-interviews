# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"Node {self.data}"


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


L1 = ListNode(1)
L1.next = ListNode(3)
L1.next.next = ListNode(5)
L1.next.next.next = ListNode(7)
L1.next.next.next.next = ListNode(9)
L1.next.next.next.next.next = ListNode(11)
L1.next.next.next.next.next.next = L1.next

L2 = ListNode(2)
L2.next = ListNode(4)
L2.next.next = ListNode(6)
L2.next.next.next = ListNode(8)
L2.next.next.next.next = ListNode(10)
L2.next.next.next.next.next = ListNode(12)
L2.next.next.next.next.next.next = L1.next.next.next


def overlapping_no_cycle_lists(L1, L2):
    """
    Test if two linked lists overlaps
    
    :type L1: ListNode
    :type L2: ListNode
    :rtype: ListNode[None]
    """
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1 # L2 is the longer list
    # Advances the longer list to get equal length lists.
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1 # None implies there is no overlap between L1 and L2.


def has_cycle(head):
    """
    Test if there is cyclicity in a linked list
   
    :type head: ListNode
    :rtype: ListNode[None]
    """
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
        
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Finds the start of the cycle.
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # Both iterators advance in tandem.
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it # iter is the start of cycle.
    return None # No cycle.