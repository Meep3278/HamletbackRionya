# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import random
from collections import defaultdict
from simanneal import Annealer
import sys

def evaluate_ordering(ordering):
    eval_list = [1 for _ in range(N)]
    for i in range(len(ordering)):
        eval_list[ordering[i][1]] += eval_list[ordering[i][0]]
    return eval_list

class GiantAnnealer(Annealer):

    def move(self):
        # choose a random entry in the matrix
        i = random.randrange(len(self.state)-1)
        self.state[i], self.state[i+1] = self.state[i+1], self.state[i]

    def energy(self):
        return -sum(evaluate_ordering(self.state))

if __name__ == '__main__':
    N = sys.argv
    try:
        len(N) == 2
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    N = int(N[1])
    init_state = [(a, b) for a in range(N) for b in range(N) if a != b]
    random.shuffle(init_state)
    ga = GiantAnnealer(init_state)
    order, total = ga.anneal()
    print(order)
    print(evaluate_ordering(order))
    print("total=" + str(-total))