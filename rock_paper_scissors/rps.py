#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # num plays = n
    # for each play
    # add all three possible results to all exisiting results

    results = [[]]
    for i in range(0, n):
        if i == 0:
          results = [['rock'], ['paper'], ['scissors']]

        if i > 0:
            new_results = []
            for result in results:
                new_results.append(result + ['rock'])
                new_results.append(result + ['paper'])
                new_results.append(result + ['scissors'])

            results = new_results

    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

