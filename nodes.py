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
L1.next = ListNode(2)
L1.next.next = ListNode(3)
L1.next.next.next = ListNode(4)
L1.next.next.next.next = ListNode(5)
L1.next.next.next.next.next = ListNode(6)
L1.next.next.next.next.next.next = ListNode(7)