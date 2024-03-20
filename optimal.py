import time
from memory_profiler import profile


@profile
def find_salary_cap(target_payroll, current_salaries):
    current_salaries.sort()
    unadjusted_salary_sum = 0.0
    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i
        adjusted_salary_sum = current_salary * adjusted_people
        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people
        unadjusted_salary_sum += current_salary
    # No solution, since target_payroll > existing payroll.
    return -1.0


def main():
    start_time = time.time()

    #test case
    print(find_salary_cap(210, [90,30,100,40,20]))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()