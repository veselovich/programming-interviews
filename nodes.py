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

def reverse_linked_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

L1 = ListNode(1)
L1.next = ListNode(3)
L1.next.next = ListNode(5)
L1.next.next.next = ListNode(7)
L1.next.next.next.next = ListNode(5)
L1.next.next.next.next.next = ListNode(3)
L1.next.next.next.next.next.next = ListNode(1)
