import time
from memory_profiler import profile


@profile
def evaluate(RPN_expression):	
    """
    Name
    Example
    
    :type x: int
    :rtype: int
    """
    intermediate_results = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y, '*':
        lambda y, x: x * y, '/': lambda y, x: int (x / y)
    }
    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(OPERATORS[token](
                intermediate_results.pop(), intermediate_results.pop()))
        else: # token is a number.
            intermediate_results.append(int(token))
    return intermediate_results[-1]



def main():
    start_time = time.time()

    #test case
    print(evaluate("3,4,+,2,*,1,+"))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()