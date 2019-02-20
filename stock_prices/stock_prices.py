#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # start a marker equal to the first price
    low_marker = prices[0]
    # start a record of the largest price difference
    record_difference = 0

    # for every number in prices
    for i in range(0, len(prices)):
        # compare the amount of the marker number to the iterator number
        # if the iterator number is lower than the marker number
        # move the marker
        if low_marker > prices[i]:
            low_marker = prices[i]
        else:
            # if it is higher than the marker number
            # measure the difference between the iterator number and the marker number
            # if that number is larger than the record replace the record
            if record_difference < prices[i] - low_marker:
                record_difference = prices[i] - low_marker
    # continue doing this until all prices have been checked

    # return the record number
    return record_difference

print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))