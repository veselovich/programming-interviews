import math
import time
from memory_profiler import profile


class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)
        
    def __lt__(self, other):
        return self.val < other. val
    
    def __eq__(self, other):
        return self.val == other.val


@profile
def generate_first_k_a_b_sqrt2(k):
    # Will store the first k numbers of the form a + b sqrt (2) .
    cand = [ABSqrt2 (0, 0)]
    i = j = 0
    for _ in range(1, k):
        cand_i_plus_1 = ABSqrt2(cand[i].a + 1, cand[i]. b)
        cand_j_plus_sqrt2 = ABSqrt2(cand[j].a, cand[j].b + 1)
        cand.append(min(cand_i_plus_1, cand_j_plus_sqrt2))
        if cand_i_plus_1.val == cand[-1].val:
            i += 1
        if cand_j_plus_sqrt2.val == cand [-1].val:
            j += 1
    return [a.val for a in cand]


def main():
    start_time = time.time()

    #test case
    print(generate_first_k_a_b_sqrt2(10))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()