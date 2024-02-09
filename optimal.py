import time
from memory_profiler import profile

from nodes import tree

@profile
def inorder_traversal(tree):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # We came down to tree from prev.
            if tree.left: # Keep going left.
                next = tree.left
            else:
                result.append(tree.data)
                # Done with left, so go right if right is not empty. Otherwise,
                # go up.
                next = tree.right or tree.parent

        elif tree.left is prev:
            # We came up to tree from its left child.
            result.append (tree.data)
            # Done with left, so go right if right is not empty. Otherwise, go
            # up.
            next = tree.right or tree.parent
        else: # Done with both children, so move up.
            next = tree.parent
        prev, tree = tree, next
    return result


def main():
    start_time = time.time()

    #test case
    print(inorder_traversal(tree.root))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()