import time
from memory_profiler import profile


@profile
def buy_and_sell_stock_twice(prices):
    """
    Buy and sell stock twice. Same day buy is not accepted
    
    
    :type x: int
    :rtype: int
    """
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that
    # day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we make the
    # second buy on that day.
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i - 1])
    return max_total_profit


def main():
    start_time = time.time()

    #test case
    prices = [12,11,13,9,12,8,14,13,15]
    print(buy_and_sell_stock_twice(prices))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()