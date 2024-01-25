import time
from memory_profiler import profile


@profile
def shortest_equivalent_path(path):
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    if not path:
        raise ValueError('Empty string is not a valid path.')
    path_names = [] # Uses list as a stack.
    # Special case: starts with '/', which is an absolute path.
    if path [0] == '/':
        path_names.append('/')
    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        else: # Must be a name.
            path_names.append(token)
    result = '/'.join(path_names)
    return result[result.startswith('//'):] # Avoid starting '//'.


def main():
    start_time = time.time()

    #test case
    print(shortest_equivalent_path('../../scripts/../local//scripts/././'))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()