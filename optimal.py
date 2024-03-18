import collections
import time
from memory_profiler import profile

Person = collections.namedtuple('Person', ('name', 'age'))

@profile
def group_by_age(people):
    age_to_count = collections.Counter([person.age for person in people])
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[to_age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        # Use age_to_count to see when we are finished with a particular age.
        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]


def main():
    start_time = time.time()

    #test case
    people = [Person('Greg', 14),
              Person('John', 12),
              Person('Andy', 11),
              Person('Jim', 13),
              Person('Phil', 12),
              Person('Bob', 13),
              Person('Chip', 13),
              Person('Tim', 14),
              ]
    group_by_age(people)
    print(people)

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()