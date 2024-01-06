import time
from memory_profiler import profile

from nodes import *


@profile
def deletion_from_list(node_to_delete):
    """
    Delete node
    
    :type node_to_delete: ListNode
    :rtype: None
    """
    if node_to_delete.next is not None:
        node_to_delete.data = node_to_delete.next.data  # Copy data from the next node to the current node
        node_to_delete.next = node_to_delete.next.next  # Update the next pointer to skip the next node
    else:
        # Handle the case where the current node is the last node in the list
        node_to_delete.data = None


def main():
    start_time = time.time()

    #test case
    deletion_from_list(L1.next.next)
    print_list(L1)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()