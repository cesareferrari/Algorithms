#!/usr/bin/python

'''
find_max_profit

input: 
    list of stock prices
    list of integers
    example: 1050 270 1540 3800 2
    example with negative profit: 100 90 80 50 20 10

output:
    signed integer, example: 3530, or -10
    3530 is the difference between 3800 - 270
    270 is the lowest price that comes before 3800

    -10 is the difference between 90 - 100 in the second example

    maximum profit that can be made from a single buy and sell
    must buy first before selling, meaning that we can't subtract from a later
    number, like we can't do 3800 - 2, which comes later;


current_min_price_so_far
max_profit_so_far

'''

import argparse


# passes tests except negative profit

def find_max_profit(prices):
    cur_min_price = prices[0]
    cur_max_profit = prices[1] - prices[0]

    for i in range(0, len(prices)):
        if prices[i] < cur_min_price:
            cur_min_price = prices[i]

        if (prices[i] - cur_min_price) > cur_max_profit:
            cur_max_profit = (prices[i] - cur_min_price)

    return cur_max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
