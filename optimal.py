import time
from memory_profiler import profile


@profile
def buy_and_sell_stock_once(prices):
    """
    Given array representing a stock price. Maximize profit from one trade
    Example: [310,315,275,295,260,270,290,230,255,250] -> 30
    
    :type prices: list
    :rtype: int
    """
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


def main():
    start_time = time.time()

    #test case
    prices = [310,315,275,295,260,270,290,230,255,250]
    print(buy_and_sell_stock_once(prices))

    end_time = time.time()
    print(f"\nExecution time: {end_time - start_time:.2}s")


if __name__ == '__main__':
    main()