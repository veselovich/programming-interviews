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


def merge_two_sorted_lists(L1, L2):
    """
    Merges two sorted linked list into a one
    
    :type L1: ListNode
    :type L2: ListNode
    :rtype: ListNode
    """
    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


L1 = ListNode(1)
L1.next = ListNode(13)
L1.next.next = ListNode(11)
L1.next.next.next = ListNode(7)
L1.next.next.next.next = ListNode(9)
L1.next.next.next.next.next = ListNode(11)
L1.next.next.next.next.next.next = ListNode(13)
L1.next.next.next.next.next.next.next = ListNode(5)