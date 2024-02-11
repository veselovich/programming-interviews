import time
from memory_profiler import profile

from nodes import root_tree

@profile
def construct_right_sibling(tree):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            # Populate left child's next field.
            start_node.left.next = start_node.right
            # Populate right child's next field if iter is not the last node of
            # level.
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next
    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left


def main():
    start_time = time.time()

    #test case
    construct_right_sibling(root_tree)
    print(root_tree.left.right.next)
    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()