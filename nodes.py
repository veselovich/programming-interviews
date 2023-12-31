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


L = ListNode(1)
L.next = ListNode(2)
L.next.next = ListNode(3)
L.next.next.next = ListNode(4)
L.next.next.next.next = ListNode(5)
L.next.next.next.next.next = ListNode(6)
L.next.next.next.next.next.next = ListNode(7)